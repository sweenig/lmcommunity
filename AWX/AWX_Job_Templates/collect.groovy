import com.santaba.agent.groovyapi.http.HTTP
import groovy.json.JsonSlurper

def hostname = hostProps.get("system.hostname")
def password=hostProps.get("awx.pass")
def username=hostProps.get("awx.user")
def port = hostProps.get("awx.port") ? hostProps.get("awx.port").toInteger() : 80

httpClient = HTTP.open(hostname, port)

headers = [
  "Authorization": "Basic ${"${username}:${password}".bytes.encodeBase64().toString()}",
  "Content-Type": "application/json"
]

url = "http://${hostname}/api/v2/job_templates/"
response = httpClient.get(url,headers)
if  (httpClient.getStatusCode() != 200 ) { println(response);return 1; }
objects = new JsonSlurper().parseText(httpClient.getResponseBody())
objects.results.each{job ->
  println("${job.id}.failures: ${(job.summary_fields.last_job.failed == "true") ? 1 : 0}")
}
return 0