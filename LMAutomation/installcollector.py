from __future__ import print_function
from pprint import pprint
import argparse

parser = argparse.ArgumentParser()
for keyword in ['company','lmaccessid','lmaccesskey','collectorId','osAndArch']:
  parser.add_argument(f"--{keyword}", required=True)
parser.add_argument("--verbose",action="store_true")
args = parser.parse_args()

import logicmonitor_sdk
import os, sys, stat

print("Setting up environment...",end="")
credentials = logicmonitor_sdk.Configuration()
credentials.company = args.company
credentials.access_id = args.lmaccessid
credentials.access_key = args.lmaccesskey
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(credentials))
print("Done")

try:
  collectorId = args.collectorId
  osAndArch = args.osAndArch

  print(f"Downloading installer for collector {collectorId} ({osAndArch})...",end="")
  installer = api_instance.get_collector_installer(collectorId,osAndArch)
  f = open('apidownloadedinstaller.bin', 'wb')
  f.write(installer.read())
  f.close()
  print("Done")

  print("Executing downloaded file...",end="")
  os.chmod('apidownloadedinstaller.bin', 0o0777)
  cmd = './apidownloadedinstaller.bin -y > pythoninstall.log'
  os.system(cmd)
  print("Done")

  if args.verbose:
    f = open("pythoninstall.log","r")
    print(f.read())
    f.close()
except logicmonitor_sdk.ApiException as e:
  print(f"Exception when calling LMApi: {e}")
