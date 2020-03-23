import groovy.json.JsonSlurper

hostname = hostProps.get("system.hostname")
short_name = hostname.split("\\.")[1]

String getResult = new URL("https://${short_name}.statuspage.io/api/v2/summary.json").text

my_json = new JsonSlurper().parseText(getResult)

println "statusio_key=" + my_json['page']['id']

return 0;