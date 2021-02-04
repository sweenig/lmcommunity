/*******************************************************************************
 *  © 2007-2019 - LogicMonitor, Inc. All rights reserved.
 ******************************************************************************/
import com.santaba.agent.groovyapi.http.HTTP
import groovy.json.JsonSlurper
import groovy.time.*

communityUser = instanceProps.get("wildvalue")
//communityUser = 1586
apitoken = hostProps.get("lmcomm.key")
resourcePath = "/core/members/${communityUser}"

try {
  httpClient = HTTP.open("communities.logicmonitor.com", 443)
  headers = ["Authorization": "Basic ${"${apitoken}:".bytes.encodeBase64().toString()}"]
  url = "https://communities.logicmonitor.com/api/${resourcePath}"
  getResponse = httpClient.get(url, headers)
  body = httpClient.getResponseBody()
}
catch (Exception e) {println("Failure to fetch data from API.");println e;return 1}
finally {httpClient.close()}

try {
  response_obj = new JsonSlurper().parseText(body)
} catch (Exception e) {println("Failure to parse JSON.");println e; return 2}

try {
  println("posts: ${response_obj.posts}")
  println("profileViews: ${response_obj.profileViews}")
  println("reputationPoints: ${response_obj.reputationPoints}")

  def lastActivity = TimeCategory.minus(new Date(), Date.parse("yyy-MM-dd'T'HH:mm:ss'Z'",response_obj.lastActivity, TimeZone.getTimeZone("UTC")))
  println("lastActivity: ${lastActivity.getDays()*24 + lastActivity.getHours() + lastActivity.getMinutes()/60}")

  def lastPost = TimeCategory.minus(new Date(), Date.parse("yyy-MM-dd'T'HH:mm:ss'Z'",response_obj.lastPost, TimeZone.getTimeZone("UTC")))
  println("lastPost: ${lastPost.getDays()*24 + lastPost.getHours() + lastPost.getMinutes()/60}")

  def lastVisit = TimeCategory.minus(new Date(),Date.parse("yyy-MM-dd'T'HH:mm:ss'Z'",response_obj.lastVisit, TimeZone.getTimeZone("UTC")))
  println("lastVisit: ${lastVisit.getDays()*24 + lastVisit.getHours() + lastVisit.getMinutes()/60}")

  def joined = TimeCategory.minus(new Date(),Date.parse("yyy-MM-dd'T'HH:mm:ss'Z'",response_obj.joined, TimeZone.getTimeZone("UTC")))
  println("joined: ${joined.getDays() + joined.getHours()/24 + joined.getMinutes()/24/60}")

  return 0
} catch (Exception e) {println("Failure to parse output.");println e; return 3}
