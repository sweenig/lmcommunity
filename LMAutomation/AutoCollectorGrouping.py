#!/usr/bin/env python3

################################################
# (C) 2020 - Stuart Weenig, All rights reserved
################################################
from pprint import pprint
import argparse, subprocess, sys

try:
    import logicmonitor_sdk
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "logicmonitor_sdk"])
    print("logicmonitor_sdk was not installed. An attempt has been made to install it.\nTry again now that it is installed.")
    quit()

##########################
# ARGUMENT PARSING
##########################
my_parser = argparse.ArgumentParser(usage=argparse.SUPPRESS)
my_parser.add_argument("-d","--debuglevel", default=0, type=int, help="Debugging verbosity: 0-∞, higher number means more verbose output.\nN A value of -1 will produce output suitable for DS output.")
my_parser.add_argument("-s","--cascadeSDT", action='store_true', help="Add a flag to each collector group that disables alerting for all devices in that group if the collector is in SDT")
for arg in ['company','access_id','access_key']:
    my_parser.add_argument("--" + arg, type=str, required=True)
try:
    args = my_parser.parse_args()
except SystemExit:
    my_parser.print_help()
    raise

cascadeSDT = args.cascadeSDT
debug = args.debuglevel

##########################
# Global counters for DS output
##########################
parent_group_created = 0 # increments if /Devices by Collector group had to be created
collector_group_group_created = 0 # increments if collector group groups had to be created
collector_dynamic_group_created = 0 # increments if collector dynamic group had to be created
c_alert_e2d = 0 # number of collectors whose devices were switched from alerting enabled to alerting disabled
c_alert_d2e = 0 # number of collectors whose devices were switches from alerting disabled to alerting enabled
c = 0 # total number of collectors


##########################
# Setup API Connection
##########################
configuration = logicmonitor_sdk.Configuration()
configuration.company = args.company
configuration.access_id = args.access_id
configuration.access_key = args.access_key
api = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))

##########################
# MAIN PROGRAM
##########################
try:
    ##########################
    # Build groups if they dont' exist
    ##########################
    # Validate/create the parent group
    if debug >= 1: print("Checking if parent group exists...")
    parentResourceGroup = api.get_device_group_list(filter="name:\"Devices by Collector\"",size=1000)
    if len(parentResourceGroup.items) > 0:
        parentResourceGroupId = parentResourceGroup.items[0].id
        if debug >= 1: print(f"Parent group exists (id={parentResourceGroupId}).")
    else:
        parentResourceGroup = api.add_device_group({"name":"Devices by Collector","parentId":1})
        parentResourceGroupId = parentResourceGroup.id
        parent_group_created += 1
        if debug >= 0: print(f"Parent group didn't exist. Created it. (id={parentResourceGroup.id})")
    if debug >= 4: print(parentResourceGroup)

    # Get the list of child groups under the parent
    collectorResourceGroupList = api.get_device_group_list(filter=f"parentId:{parentResourceGroupId}")
    if debug >= 4: print(collectorResourceGroupList)
    collectorResourceGroups = {x.name : x for x in collectorResourceGroupList.items}
    if debug >= 2:
        for k,v in collectorResourceGroups.items():
            print(f"Collector resource group: {k}")
            if debug >= 3:
                for j,u in v.to_dict().items(): print(f"  {j}: {u}")

    # Fetch the collector groups
    if debug >= 1: print("Fetching collector groups...")
    collectorRealGroupList = api.get_collector_group_list(fields="id,name,description,numOfCollectors",size=1000)
    collectorRealGroups = {x.name : x for x in collectorRealGroupList.items}
    if debug >= 2:
        for k,v in collectorRealGroups.items():
            print(f"Collector group: {k}")
            if debug >= 3:
                for j,u in v.to_dict().items(): print(f"  {j}: {u}")

    # validate/create the collector groups as resource groups
    if debug >= 1: print("Validating/creating collector resource groups...")
    if debug >= 2: print(f"Collector Resource Groups: {collectorResourceGroups.keys()}")
    for k,v in collectorRealGroups.items():
        if debug >= 2: print(f"Checking that resource group for \"{k}\" exists...")
        if k in collectorResourceGroups.keys():
            if debug >= 2: print(f"  Collector resource group exists for collector \"{k}\"")
        else:
            if debug >= 1: print(f"  Collector resource group doesn't exist for collector \"{k}\"")
            newCollectorResourceGroup = api.add_device_group({"name":k, "parentId": parentResourceGroupId})
            collector_group_group_created += 1
            if debug >= 1: print(f"  Collector resource group didn't exist. Created it ({newCollectorResourceGroup.id})")

    # refresh the collector resource group list
    collectorResourceGroupList = api.get_device_group_list(filter=f"parentId:{parentResourceGroupId}")
    if debug >= 4: print(collectorResourceGroupList)
    collectorResourceGroups = {x.name : x for x in collectorResourceGroupList.items}

    # Get the list of collectors (with all their attributes)
    collectorList = api.get_collector_list()
    c = len(collectorList.items)
    if debug >= 1: print(f"{len(collectorList.items)} collectors found.")
    for collector in collectorList.items:
        if debug >= 3:
            for collector in collectorList.items: print(collector)
        if debug >= 0: print(f"Inspecting collector \"{collector.description}\" (Group: \"{collector.collector_group_name}\")")
        collectorCleanDescription = collector.description.replace("\\","_").replace(",","_")
        if debug >= 2:
            print(f"  Checking if dynamic group exists for collector {collector.description}")
            if debug >= 3:
                for x in collectorResourceGroups[collector.collector_group_name].sub_groups:
                    print(f"{x.id}: {x.name} ({x.applies_to})")
        if collectorCleanDescription in [x.name for x in collectorResourceGroups[collector.collector_group_name].sub_groups]:
            whichgroup = [x.name for x in collectorResourceGroups[collector.collector_group_name].sub_groups].index(collectorCleanDescription)
            collectorResourceGroupId = collectorResourceGroups[collector.collector_group_name].sub_groups[whichgroup].id
            collectorResourceGroupAppliesTo = collectorResourceGroups[collector.collector_group_name].sub_groups[whichgroup].applies_to
            if debug >= 1: print(f"  {collector.description} dynamic group exists under {collector.collector_group_name} resource folder.")
            if debug >= 2: print(f"  Checking appliesTo for resource group \"{collectorCleanDescription}\" (id: {collectorResourceGroupId})")
            if collectorResourceGroupAppliesTo != f"system.prefcollectorid == \"{collector.id}\"":
                if debug >= 1: print(f"  AppliesTo expression is not correct: {collectorResourceGroupAppliesTo}")
                id = collectorResourceGroupId
                body = {"name":collectorCleanDescription, "appliesTo": f"system.prefcollectorid == \"{collector.id}\""}
                result = api.patch_device_group_by_id(id,body)
                if debug >= 0: print(f"  {collector.description} group at \"{result.full_path}\" with id {id} updated to have the correct AppliesTo: {result.applies_to}")
                if debug >= 4: print(result)
            else:
                if debug >= 1: print(f"  AppliesTo expression is correct. No changes needed.")
        else:
            if debug >= 1: print(f"  Could not find a resource group for \"{collectorCleanDescription}\"")
            body = {
                "name":collectorCleanDescription,
                "parentId": collectorResourceGroups[collector.collector_group_name].id,
                "appliesTo": f"system.prefcollectorid == \"{collector.id}\""
            }
            if debug >= 4: pprint(body)
            result = api.add_device_group(body)
            collector_dynamic_group_created += 1
            if debug >= 0: print(f"  {collector.description} group created at {result.full_path} with id {result.id}")
            if debug >= 4: print(result)

    #refresh the collector group list
    collectorResourceGroupList = api.get_device_group_list(filter=f"fullPath~\"Devices by Collector/*/*\"")
    if debug >= 4: print(collectorResourceGroupList)
    collectorResourceGroups = {x.name : x for x in collectorResourceGroupList.items}
    if debug >= 3:
        for k,v in collectorResourceGroups.items():
            print(f"{k}:\n  {v}")

    ##########################
    # Cascade SDT from collector to devices it monitors
    ##########################
    if cascadeSDT:
        for collector in collectorList.items:
            if debug >= 0: print(f"Synchronizing SDT from \"{collector.description}\" to devices (enable/disable alerting)")
            #put the group in SDT (not really, just disable alerting) if the collector's in SDT
            collectorCleanDescription = collector.description.replace("\\","_").replace(",","_")
            id = collectorResourceGroups[collectorCleanDescription].id
            body = collectorResourceGroups[collectorCleanDescription]
            if collector.in_sdt:
                if debug >= 1: print(f"  Collector {collector.description} is in SDT.")
                if collectorResourceGroups[collectorCleanDescription].disable_alerting == False:
                    if debug >= 1: print(f"  Setting group {collectorResourceGroups[collectorCleanDescription].id} to not alarm.")
                    body.disable_alerting = True
                    result = api.update_device_group_by_id(id,body)
                    c_alert_e2d += 1
                    if debug >= 0: print(f"  {collector.description} is now in SDT. {result.full_path} group updated to disable alerting.")
                    if debug >= 4: print(result)
                else:
                    if debug >= 1: print(f"  {collector.description} group alerting is already disabled.")
            else:
                if debug >= 1: print(f"  Collector {collector.description} is not in SDT.")
                if collectorResourceGroups[collectorCleanDescription].disable_alerting == True:
                    if debug >= 1: print(f"  Setting group {collectorResourceGroups[collectorCleanDescription].id} to not alarm.")
                    body.disable_alerting = False
                    result = api.update_device_group_by_id(id,body)
                    c_alert_d2e += 1
                    if debug >= 0: print(f"  {collector.description} is no longer in SDT. {result.full_path} group updated to enable alerting.")
                    if debug >= 4: print(result)
                else:
                    if debug >= 1: print(f"  {collector.description} group alerting is already enabled.")
    else:
        print("Not cascading collector SDTs to the devices they are monitoring")

    if debug < 0:
        print(f"parent_group_created: {parent_group_created}")
        print(f"collector_group_group_created: {collector_group_group_created}")
        print(f"collector_dynamic_group_created: {collector_dynamic_group_created}")
        print(f"c_alert_e2d: {c_alert_e2d}")
        print(f"c_alert_d2e: {c_alert_d2e}")
        print(f"c: {c}")

except logicmonitor_sdk.rest.ApiException as e:
    print(f"Exception when calling LMApi: ${e}")
