# Devices by Collector Auto Group Sorter

This can be used either by itself or as part of a DataSource. The Python script automatically creates/updates a "Devices by Collector" group under the root. Under that, it creates/updates groups paralleling the Collector groups (from the Collectors page). Under those, creates/updates a dynamic group for each Collector with AppliesTo to include devices monitored by that Collector.

It also synchronizes SDT from Collector to the devices that Collector monitors by disabling alerting on the Collector dynamic group. If you put the Collector into SDT, it will disable alerting on that Collector's groups, thus disabling alerting on the device monitored by that Collector.

## Installation

Requires Python3 and the logicmonitor_sdk library, which isn't installed on the collector by default. Every time it runs, the script will attempt to install it if it's missing, then exit. The second run should be successful if the installation was successful.

## Usage

The following arguments are required: --company, --access_id, --access_key
optional arguments:
  -h, --help            show this help message and exit
  -d DEBUGLEVEL, --debuglevel DEBUGLEVEL
                        Debugging verbosity: 0-∞, higher number means more
                        verbose output. N A value of -1 will produce output
                        suitable for DS output.
  -s, --cascadeSDT      Add a flag to each collector group that disables
                        alerting for all devices in that group if the
                        collector is in SDT
  --company COMPANY
  --access_id ACCESS_ID
  --access_key ACCESS_KEY

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
