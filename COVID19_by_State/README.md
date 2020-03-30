# Simple COVID-19 By State DS
Simple DS to track COVID-19 cases and deaths broken out by state. It started out [written by mkerfoot on the communities](https://communities.logicmonitor.com/topic/5378-covid-19/). I adapted it to run in Groovy so it can be collected by any collector.

In addition to allowing it to run on non-Windows collectors, I also converted it into BATCHSCRIPT instead of SCRIPT. This has the added benefit that the collection happens only once per poll interval vs. once per instance per poll interval.

This groups by country, but it is a manual thing, looking up the states in a hard coded country to state map. If an entry is not found to be either in Canada or one of the other "states", it's assumed to be a state in the U.S.

This uses what's quickly become one of my standard practices for discovery filters. I have begun including both an include and an exclude (by RegEx) discovery filter on most of my DSs. This allows you to apply the DS to multiple resources and have different discovery rules for each one.

Simply set two properties on the device this applies to (easiest to just add Finnhub.io as an API resource, but could just as easily be a customer collector):
* COVID19_by_State.includeRegex: set this to a valid RegEx expression for states you want included. E.g. `New York|California|Texas|Florida`. If you want to include everything, set it to `.*`.
* COVID19_by_State.excludeRegex: set this to a valid RegEx expression for states you want excluded. E.g. `Wyoming`.

Set a different value for these properties on a different device and you'll get different items discovered. One way this could be used would be to have some states tracked for one customer and some states tracked for a different customer.
