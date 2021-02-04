# lmwrapper

lmwrapper is a Python library for simplifying interaction with the LogicMonitor API. It uses the LogicMonitor Python SDK, but takes it a step further by facilitating credentials management. All credentials are stored in a JSON file called creds.json that looks like this:

```json
{
  "lmstuartweenig": {
    "API_ACCESS_ID": "adelarthrosomatous",
    "API_ACCESS_KEY": "zygomaticoauricularis",
    "COMPANY_NAME": "lmstuartweenig"
  },
  "traininglab": {
    "API_ACCESS_ID": "adelarthrosomatous",
    "API_ACCESS_KEY": "zygomaticoauricularis",
    "COMPANY_NAME": "traininglab"
  }
}
```

If only one set of credentials is needed, the JSON file would look like this:
```json
{
  "lmstuartweenig": {
    "API_ACCESS_ID": "adelarthrosomatous",
    "API_ACCESS_KEY": "zygomaticoauricularis",
    "COMPANY_NAME": "lmstuartweenig"
  }
}

```

## Installation

Just put the file [lm.py](../blob/main/lm.py) into the same directory as the creds.json file. You'll either need to have the [logicmonitor_sdk](https://www.logicmonitor.com/support/rest-api-developers-guide/logicmonitor-sdks) installed or downloaded into the current directory. A copy (which could be outdated) is included in this repo.

## Setup
You can use this tool either in a script or in the interpreter. Either way, once you've got the credentials file setup, getting started only takes one line:

```python
>>> from lm import lm
```

## Usage
If you are using this utility in a script, your credentials file should contain only one entry, unless you are running the script interactively (I have plans to safeguard against this).

If multiple sets of credentials are found in the credentials file, you will be prompted for which set you want to use. Simply return the number (index) of the set you want to use, then you can call any of the [published SDK methods](https://www.logicmonitor.com/support-files/rest-api-developers-guide/sdks/docs/) against the `lm` object. The example below uses the [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) style of getting the output. You could just as easily pprint it or store the results in a variable.

```python
>>> from lm import lm
The following credentials were found in creds.json.
0. lmstuartweenig
1. traininglab
Which one would you like to use? 0
>>> lm.get_device_list()
{'items': [{'auto_properties': [{'name': 'predef.externalResourceID',
                                 'value': '06:57:9f:e2:63:b8'},
                                {'name': 'auto.eri.override', 'value': '1'},
                                {'name': 'auto.product.name', 'value': 'null'},
                                {'name': 'auto.idledays', 'value': '98'},
                                {'name': 'auto.ip.v4.routing_enabled',
                                 'value': 'false'},
                                {'name': 'auto.enterprise_number',
                                 'value': '8072'},
                                {'name': 'auto.endpoint.uptime',
                                 'value': '482 days, 22:17:23.40'},
                                {'name': 'auto.memory.total',
                                 'value': '8373010432'},
---OUTPUT TRUNCATED---

```

If your credentials file only has one set of credentials, the selection will default to using that one set of credentials.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Attributions
Special thanks go to the following for spawning the idea, method, and benefits:

- Michael Leo at Harvard University
- Stefan Wuensch at Harvard University
