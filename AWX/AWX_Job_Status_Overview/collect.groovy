import com.santaba.agent.groovyapi.http.HTTP
import groovy.json.JsonSlurper

def hostName = hostProps.get("system.hostname")
def password=hostProps.get("awx.pass")
def username=hostProps.get("awx.user")
def port = hostProps.get("awx.port") ? hostProps.get("awx.port").toInteger() : 80

httpClient = HTTP.open(hostName, port)

url = "http://"+hostName+"/api/v2/dashboard/graphs/jobs/"
headers = [
  "Authorization": "Basic ${"${username}:${password}".bytes.encodeBase64().toString()}",
  "Content-Type": "application/json"
]
response = httpClient.get(url,headers)
if  (httpClient.getStatusCode() != 200 ) { println(response);return 1; }
objects = new JsonSlurper().parseText(httpClient.getResponseBody())
println("successful: ${objects.jobs.successful[-1][1]}")
println("failed: ${objects.jobs.failed[-1][1]}")

return 0