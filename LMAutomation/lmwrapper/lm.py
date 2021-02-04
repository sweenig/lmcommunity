import logicmonitor_sdk, json
from os import path
import __main__ as main

credsfile = "creds.json"

if path.exists(credsfile):
    with open(credsfile) as f: creds = json.load(f)
    if len(creds) == 0:
        print(f"No credentials found in file {credsfile}.")
    elif len(creds) == 1 or hasattr(main,'__file__'):
        creds = list(creds.values())[0]
    elif len(creds) > 1:
        print(f"The following credentials were found in {credsfile}.")
        for i, key in enumerate(creds): print(f"{i}. {key}")
        try:
            credidx = int(input("Which one would you like to use? "))
        except KeyboardInterrupt:
            print("\n")
            quit()
        creds = list(creds.values())[credidx]
    configuration = logicmonitor_sdk.Configuration()
    configuration.company           = creds['COMPANY_NAME']
    configuration.access_id         = creds['API_ACCESS_ID']
    configuration.access_key        = creds['API_ACCESS_KEY']
    lm = logicmonitor_sdk.LMApi( logicmonitor_sdk.ApiClient( configuration ) )
else:
    print(f"File not found: {credsfile}")
    print("""Create a config file called creds.json in this directory that looks like this:
{
  "API_ACCESS_ID": "adelarthrosomatous",
  "API_ACCESS_KEY": "zygomaticoauricularis",
  "COMPANY_NAME": "yourportalname"
}""")
    lm = ""


# % python3
# Python 3.9.1 (default, Jan  8 2021, 17:15:36)
# >>> from lm import lm
# >>> lm.get_website_list(size=1)
# {'items': [{'alert_expr': '< 14 7 4',
#             'checkpoints': [{'geo_info': 'Overall',
#                              'id': 15675125,
#                              'smg_id': 0},
#                             {'geo_info': 'US - Washington DC',
#                              'id': 15675123,
#                              'smg_id': 2},
#                             {'geo_info': 'US - Oregon',
# (etc. etc. etc.)


# read-only-creds.json
# {
#     "API_ACCESS_ID": "adelarthrosomatous",
#     "API_ACCESS_KEY": "zygomaticoauricularis",
#     "COMPANY_NAME": "lmstuartweenig"
# }
