/*******************************************************************************
 *  © 2007-2019 - LogicMonitor, Inc. All rights reserved.
 ******************************************************************************/
import com.santaba.agent.groovyapi.http.HTTP
import groovy.json.JsonSlurper
import groovy.time.*

communityUsers = hostProps.get("lmcomm.userid").tokenize(", |")
apitoken = hostProps.get("lmcomm.key")
resourcePath = "/core/members/?perPage=500"

try {
  httpClient = HTTP.open("communities.logicmonitor.com", 443)
  headers = ["Authorization": "Basic ${"${apitoken}:".bytes.encodeBase64().toString()}"]
  url = "https://communities.logicmonitor.com/api/${resourcePath}"
  page = 1
  max_size = 9999999999999
  userdata = []
  while (userdata.size() < max_size){
    getResponse = httpClient.get(url + "&page=${page}", headers)
    body = httpClient.getResponseBody()
    response_obj = new JsonSlurper().parseText(body)
    userdata += response_obj.results
    fetched = response_obj.results.size()
    max_size = response_obj.totalResults.toInteger()
    //println("Fetched ${fetched} of ${max_size} (${max_size - userdata.size()} remaining)")
    page += 1
  }
  userdata.each{
    if (communityUsers.contains(it.id.toString())){
      println("${it.id}##${it.name} (${it.email})######primaryGroup=${it.primaryGroup.name}")
    } else {
      //println("${it.name} isn't interesting ${it.id}.")
    }
  }
  return 0
}
catch (Exception e) {println e;return 1}
finally {httpClient.close()}
