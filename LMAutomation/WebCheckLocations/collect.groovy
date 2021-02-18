import groovy.json.JsonSlurper

page = new URL("https://s3.amazonaws.com/logicmonitor-marketing/sitemonitor_ips.json?_ga=2.37320611.289127943.1612793504-851486786.1607022888").getText()

instances = new JsonSlurper().parseText(page)

instances.Logicmonitor_Sitemonitor_Machines.Public_IPs.each{println("${it.ip}_${it.location.replaceAll(" ","")}.value=1")}

return 0