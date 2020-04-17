# Process monitoring

These datasources allow monitoring of [Windows Services](Win_Service_Select/Win_Service_Select.xml), [Windows Processes](Win_Process_Stats_Groovy/Win_Process_Stats_Groovy.xml) and on [Linux](Linux_SSH_Processes_Select/Linux_SSH_Processes_Select.xml).

The DataSources work without having to manually specify the processes/services one by one on each server.  Instead, they use active discovery to find the processes. However, since monitoring all processes/services on every server tends to bog down the collector, these datasources also include the ability to manipulate discovery using properties, as follows:

1. For [Win_Service_Select](Win_Service_Select/Win_Service_Select.xml) and [Win_Service_Select_Groovy](Win_Service_Select_Groovy/Win_Service_Select_Groovy.xml):
  * Win_Service_Select.includeRegEx
  * Win_Service_Select.excludeRegEx
2. For [Win_Process_Stats_Groovy](Win_Process_Stats_Groovy/Win_Process_Stats_Groovy.xml):
  * Win_Process_Stats.excludeRegEx
  * Win_Process_Stats.includeRegEx
3. For [Linux_SSH_Processes_Select](Linux_SSH_Processes_Select/Linux_SSH_Processes_Select.xml):
  * Linux_SSH_Processes_Select.includeRegEx
  * Linux_SSH_Processes_Select.excludeRegEx

These properties are referenced in the discovery filters of each datasource. You would need to set these properties on each device you want these datasources to apply to. I recommend setting them as properties on a group containing the servers (/Devices by Type/Linux Servers or /Devices by Type/Windows Servers for example). In my portal, since I want all servers to have the same filters, I just set these properties on the root folder so they are inherited by all devices. The ones that don't need the property won't use them.

The values of the properties need to be RegEx expressions that match on the processes desired. Starting with the simple case of wanting to monitor everything, you could set the following properties (I'm showing Windows, but the method is the same for all):
`Windows_Service_Select.includeRegEx = .*`
`Windows_Service_Select.excludeRegEx = DO NOT EXCLUDE ANYTHING`
These two properties would cause everything (.* matches everything in RegEx) to be included and nothing to be excluded, unless there were a service called "DO NOT EXCLUDE ANYTHING" (spoilers: there's probably not).

On a Windows server I have the following properties set. Notice that the include property is inherited from a parent group, but the exclude property is specifically set on this device, overriding the exclude property from the parent.

![example1](example1.png "Example")

This results in discovery filtering out a few services (along with a bunch that are filtered out because they don't start automatically):

![example1-result](example1-result.png "Results")

Notice also that the RegEx for gupdate actually matched on two different services containing "gupdate". Keep in mind that the discovery filters are AND'ed together, so for a service to get discovered, it must pass each and every discovery filter.

## Collector Performance
If you want to monitor lots of processes/services on Windows systems, the \_Select DataSources might not be the best approach, since the large number of processes/services will cause huge numbers of tasks in the WMI queue on the collector. Instead, there are two Groovy based DataSources that will allow you to make one request for all the data for all services/processes on the system. This can cut the query count down from thousands in total to one per device.

[Win_Service_Select_Groovy](Win_Service_Select_Groovy/Win_Service_Select_Groovy.xml) and [Win_Process_Stats_Groovy](Win_Process_Stats_Groovy/Win_Process_Stats_Groovy.xml) both use BATCHSCRIPT mode to fetch all the data for all instances in a single execution of the [collection script](Win_Service_Select_Groovy/collect.groovy). This would allow a more expansive list of processes/services to be monitored without adding significant load to the collector.

Thanks to Vitor Santos for providing the basis and need for these two DataSources.
