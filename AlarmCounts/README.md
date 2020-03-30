# Datasources to gather statistics around the total number of alarms
Each DataSource does it slightly differently:
## Alarm By Group
* Counts the total number of alarms for each group in the portal.
* Meant to be applied to a single API resource in your portal (easiest to add `[portalname].logicmonitor.com` as a resource itself; turn off ping and any other DSs that don't/won't work). This DS needs an API token; set the values as properties called alarmbygroup.id, alarmbygroup.pass, & alarmbygroup.account (being your portal name).
* Set discovery filters to refine which groups are monitored. By default, the DS looks for groups that are 2 levels down from the root.
  - auto.depth: depth from the root (root having depth of 0, all direct children under the root have depth 1)
  - auto.fullPath: full path of the group (e.g. `/Customers/Customer 1/Routers`)
## Alarm Count (by DataSource)
* Counts the total number of alarms for each datasource discovered; Discovers each DS that has at least one alarm. Instances are deleted after 30 days, so it should show you only those DSs that actually have alarms (most often) while still keeping historical data for old Datasources.
* Meant to be applied to a single API resource in your portal (easiest to add `[portalname].logicmonitor.com` as a resource itself; turn off ping and any other DSs that don't/won't work). This DS needs an API token; set the values as properties called alarmCount.id, alarmCount.key & alarmCount.company (being your portal name).

## Alarm Count By Device
* Counts the total number of alarms per device, per datasource.
* Meant to be applied to all devices. Generate an API token and apply it to the root folder creating properties called AlarmCountByDevice.id, AlarmCountByDevice.key, & AlarmCountByDevice.company (being your portal name).
