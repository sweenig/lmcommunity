# Process monitoring

These two datasources allow monitoring of processes on [Windows](Win_Service_Select/Win_Service_Select.xml) and on [Linux](Linux_SSH_Processes_Select/Linux_SSH_Processes_Select.xml) without having to manually specify the processes one by one on each server.  Instead, it uses active discovery to find the processes. However, since monitoring all processes on every server tends to bog down the collector, these datasources also include the ability to manipulate discovery using properties.

In both datasources, they expect a pair of properties called
1. For Windows:
  * Win_Service_Select.includeRegEx
  * Win_Service_Select.excludeRegEx
2. For Linux:
  * Linux_SSH_Processes_Select.includeRegEx
  * Linux_SSH_Processes_Select.excludeRegEx

These properties are referenced in the discovery filters of each datasource. You would need to set these properties on each device you want these datasources to apply to. I recommend setting them as properties on a group containing the servers (/Devices by Type/Linux Servers or /Devices by Type/Windows Servers for example).

The values of the properties need to be RegEx expressions that match on the processes desired. Starting with the simple case of wanting to monitor everything, you could set the following properties (I'm showing Windows, but the method is the same for both):
`Windows_Service_Select.includeRegEx = .*`
`Windows_Service_Select.excludeRegEx = DO NOT EXCLUDE ANYTHING`
These two properties would cause everything (.* matches everything in RegEx) to be included and nothing to be excluded, unless there were a service called "DO NOT EXCLUDE ANYTHING" (spoilers: there's probably not).

On a Windows server I have the following properties set. Notice that the include property is inherited from a parent group, but the exclude property is specifically set on this device, overriding the exclude property from the parent.

![example1](example1.png "Example")

This results in discovery filtering out a few services (along with a bunch that are filtered out because they don't start automatically):

![example1-result](example1-result.png "Results")

Notice also that the RegEx for gupdate actually matched on two different services containing "gupdate". Keep in mind that the discovery filters are AND'ed together, so for a service to get discovered, it must pass each and every discovery filter.
