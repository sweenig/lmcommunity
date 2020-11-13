from __future__ import print_function
import argparse

parser = argparse.ArgumentParser()
for keyword in ['company','lmaccessid','lmaccesskey']:
  parser.add_argument(f"--{keyword}", required=True)
parser.add_argument("--verbose",action="store_true")
args = parser.parse_args()
debug = args.verbose

if debug: print("Setting up environment...",end="")
import logicmonitor_sdk
from pprint import pprint
from datetime import datetime, date, time
import json
fivepm = int(datetime.combine(date.today(),time(17)).timestamp()) * 1000
credentials = logicmonitor_sdk.Configuration()
credentials.company = args.company
credentials.access_id = args.lmaccessid
credentials.access_key = args.lmaccesskey
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(credentials))
if debug: print("Done")

try:
  if debug: print("Fetching current list of SDTs...",end="")
  sdts = api_instance.get_sdt_list(filter="type:\"CollectorSDT\"")
  if debug: print("Done.")
except logicmonitor_sdk.ApiException as e:
  print(f"Exception when fetching SDTs: {e}")

for sdt in sdts.items:
  if sdt.collector_id != 6:
    body = sdt
    body.start_date_time = fivepm
    print(f"Collector {sdt.id}")
    if debug: pprint(f"  Body: {body}")
    response = api_instance.update_sdt_by_id(sdt.id,body)
    if debug: print(f"{response}:")
  else:
    print(f"Skipping collector {sdt.collector_description}")
