# Status Page Monitoring (if it's hosted by StatusPage.io)

## To add monitoring
1. Import [the DataSource definition](StatusIOServiceStatus/StatusIOServiceStatus.xml) into your portal
2. From the status page:
  * append "/api/v2"
  * Grab the id/key from the url in the summary section (look for Endpoint followed by a URL that ends in "summary.json", the id/key is the part after "https://" and before ".statuspage.io/api/v2/summary.json")
3. Add the status page as a resource into your portal:
  * Add the FQDN of the status page as the IP/DNS
  * Make the name something friendly
  * Add a property called "statusio_key" with the id/key fetched earlier as the value

That should get the device in and discovery started. Wait a few minutes and you should see the component services discovered and data should start flowing in.

We've identified the following sites that use StatusPage.io to host their status page. We've looked up the key for you so you don't have to. This isn't an exhaustive list. If you think a status page is hosted by StatusPage.io, simpliy append "/api/v2#summary" to the status page. If that loads, you should be able to find the key. If you do find a new key, please send it our way so we can add it to our list here. If you manually enter the key, the PropertySource "StatusIOKey" isn't needed.
### Discovered Keys
|Name|URL|Key|
|---|---|---|
|Atlassian|https://metastatuspage.com|2j98763l56x|
|AWeber|https://status.aweber.com|bjqyd6ttxjk7|
|BigCommerce|https://status.bigcommerce.com|qbn4dyd29jby|
|BuzzFeed|https://status.buzzfeed.com|1cdp54tg9bv9|
|Canva|https://www.canvastatus.com|3hg3yf1shl9k|
|Canvas|https://status.instructure.com|nlxv32btr6v7|
|CloudFlare|https://www.cloudflarestatus.com|yh6f0r4529hb|
|DataDog|https://status.datadoghq.com|1k6wzpspjf99|
|DataDog Integrations|https://datadogintegrations.statuspage.io/|tbc0zy2gb6bf|
|DataDog EU|https://status.datadoghq.eu/|5by3sysm209d|
|Datto|https://status.datto.com|9wpk4y80vt4s|
|DialPad|https://status.dialpad.com|80trk830s0hg|
|DrChrono|https://status.drchrono.com|ftd21120x69r|
|Dropbox|https://status.dropbox.com|t34htyd6jblf|
|Duo Security|https://status.duo.com|qrxf5mzbrsxw|
|Fitbit|https://www.fitbitstatus.com|rcw3d4yzqkqg|
|GitHub|https://www.githubstatus.com|kctbh9vrtdwd|
|GongIO|https://status.gong.io|wr00cbpjhn6r|
|GoToMeeting|https://status.gotomeeting.com|kwzln7bn4hg8|
|Hubspot|https://status.hubspot.com|8b9w1wwq3g7d|
|Jamf|https://status.jamf.com|5z7bmx2nb2yj|
|JumpCloud|https://status.jumpcloud.com|nflr6k3n1c0h|
|Keen IO|https://status.keen.io|z3mvdbpvy7yh|
|Liberato|https://status.librato.com|636574ls1dpd|
|Logicmonitor|https://status.logicmonitor.com|vgvrd21p58vb|
|Logitech|https://status.logitech.com|zbr74ch8kcdy|
|MindBody|https://status.mindbodyonline.com|xfhhcblmbpbd|
|Monday.com|https://status.monday.com|zh081jts88wj|
|MuleSoft|https://status.mulesoft.com|rl5vblzz3gbw|
|OkCupid|https://status.okcupid.com|pqtr9kytt07d|
|PagerDuty|https://status.pagerduty.com|33yy6hwxnwr3|
|Peloton|https://status.onepeloton.com|mp8rwtf7yt9p|
|Postman|https://status.postman.com|ms1frkqnsp7r|
|ProCore|https://status.procore.com|jxb4w0vdl2tv|
|Reddit|https://www.redditstatus.com|2kbc0d48tv3j|
|Shopify|https://status.shopify.com|d33g96wd23dd|
|Showpad|https://status.showpad.com|z87gt5b68cql|
|Skilljar|https://status.skilljar.com|by5hq8p4g556|
|Sumo Logic|https://status.sumologic.com|8 keys|
|Tableau|https://trust.tableau.com|g7fqbfflg42q|
|Trello|https://trello.status.atlassian.com|h5frqhb041yq|
|Twilio|https://status.twilio.com|gpkpyklzq55q|
|Wistia|https://status.wistia.com|750cwd148kqj|
|Zoom|https://status.zoom.us/|14qjgk812kgk|
