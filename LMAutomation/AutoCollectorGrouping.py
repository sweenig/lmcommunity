################################################
# (C) 2020 - Stuart Weenig, All rights reserved
################################################
from pprint import pprint
import argparse
import logicmonitor_sdk

##########################
# ARGUMENT PARSING
##########################
my_parser = argparse.ArgumentParser(usage=argparse.SUPPRESS)
my_parser.add_argument("-d","--debuglevel", default=0, type=int, help="Debugging verbosity: 0-∞, higher number means more verbose output.")
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
    parentGroup = api.get_device_group_list(filter="name:\"Devices by Collector\"")
    if len(parentGroup.items) > 0:
        parentGroupId = parentGroup.items[0].id
        if debug >= 1: print(f"Parent group exists (id={parentGroupId}).")
    else:
        parentGroup = api.add_device_group({"name":"Devices by Collector","parentId":1})
        parentGroupId = parentGroup.id
        if debug >= 0: print(f"Parent group didn't exist. Created it. (id={parentGroup.id})")
    if debug >= 4: print(parentGroup)

    # Get the list of child groups under the parent
    collectorGroupList = api.get_device_group_list(filter=f"parentId:{parentGroupId}")
    if debug >= 4: print(collectorGroupList)
    collectorGroups = {x.name : x for x in collectorGroupList.items}
    if debug >= 2:
        for k,v in collectorGroups.items():
            print(f"Collector group: {k}")
            if debug >= 3:
                for j,u in v.to_dict().items(): print(f"  {j}: {u}")

    # Get the list of collectors (with all their attributes)
    collectorList = api.get_collector_list()
    if debug >= 1: print(f"{len(collectorList.items)} collectors found.")
    for collector in collectorList.items:
        if debug >= 3:
            for collector in collectorList.items: print(collector)
        if debug >= 0: print(f"Inspecting {collector.description}")
        collectorCleanDescription = collector.description.replace("\\","_").replace(",","_")
        if collectorCleanDescription in collectorGroups.keys():
            if debug >= 1: print(f"  {collector.description}'s collector group exists.")
            if collectorGroups[collectorCleanDescription].applies_to != f"system.prefcollectorid == \"{collector.id}\"":
                if debug >= 1: print(f"  AppliesTo expression is not correct: {collectorGroups[collectorCleanDescription].applies_to}")
                id = collectorGroups[collectorCleanDescription].id
                body = collectorGroups[collectorCleanDescription]
                body.applies_to = f"system.prefcollectorid == \"{collector.id}\""
                result = api.update_device_group_by_id(id,body)
                if debug >= 0: print(f"  {collector.description} group at {result.full_path} with id {id} updated to have the correct AppliesTo: system.prefcollectorid == \"{collector.id}\"")
                if debug >= 4: print(result)
            else:
                if debug >= 1: print(f"  AppliesTo expression is correct. No changes needed.")
        else:
            if debug >= 1: print(f"{collector.description}'s collector group doesn't exist.")
            body = {
                "name":collectorCleanDescription,
                "parentId":parentGroupId,
                "appliesTo":f"system.prefcollectorid == \"{collector.id}\""
            }
            result = api.add_device_group(body)
            if debug >= 0: print(f"  {collector.description} group created at {result.full_path} with id {result.id}")
            if debug >= 4: print(result)

        #refresh the collector group list
        collectorGroupList = api.get_device_group_list(filter=f"parentId:{parentGroupId}")
        if debug >= 4: print(collectorGroupList)
        collectorGroups = {x.name : x for x in collectorGroupList.items}

        ##########################
        # Cascade SDT from collector to devices it monitors
        ##########################
        if cascadeSDT:
            #put the group in SDT if the collector's in SDT
            id = collectorGroups[collectorCleanDescription].id
            body = collectorGroups[collectorCleanDescription]
            if collector.in_sdt:
                if debug >= 1: print(f"  Collector {collector.description} is in SDT.")
                if collectorGroups[collectorCleanDescription].disable_alerting == False:
                    if debug >= 1: print(f"  Setting group {collectorGroups[collectorCleanDescription].id} to not alarm.")
                    body.disable_alerting = True
                    result = api.update_device_group_by_id(id,body)
                    if debug >= 0: print(f"  {collector.description} is now in SDT. {result.full_path} group updated to disable alerting.")
                    if debug >= 4: print(result)
                else:
                    if debug >= 1: print(f"  {collector.description} group alerting is already disabled.")
            else:
                if debug >= 1: print(f"  Collector {collector.description} is not in SDT.")
                if collectorGroups[collectorCleanDescription].disable_alerting == True:
                    if debug >= 1: print(f"  Setting group {collectorGroups[collectorCleanDescription].id} to not alarm.")
                    body.disable_alerting = False
                    result = api.update_device_group_by_id(id,body)
                    if debug >= 0: print(f"  {collector.description} is no longer in SDT. {result.full_path} group updated to enable alerting.")
                    if debug >= 4: print(result)
                else:
                    if debug >= 1: print(f"  {collector.description} group alerting is already enabled.")
        else:
            print("Not cascading collector SDTs to the devices they are monitoring")

except logicmonitor_sdk.rest.ApiException as e:
    print(f"Exception when calling LMApi->addDevice: ${e}")
