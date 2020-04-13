import java.util.Base64
import javax.crypto.Mac
import javax.crypto.spec.SecretKeySpec
import com.santaba.agent.groovyapi.http.*
import groovy.json.JsonSlurper
import groovy.json.JsonOutput

zoom_api_key = hostProps.get("zoom_api.key")

myKey = generateJWTToken(hostProps.get("zoom_api.pass"))

httpClient = HTTP.open("https://api.zoom.us", 443)

def url = "https://api.zoom.us/v2/report/daily"

def headers = [:]
headers.put("Authorization", "Bearer " + myKey)
headers.put("Content-Type","application/json")
headers.put("User-Agent", "Zoom-Jwt-Request")

def getResponse = httpClient.get(url,headers)
def report = new JsonSlurper().parseText(httpClient.getResponseBody())

println(JsonOutput.toJson(report.dates[-1]))
return 0


public String generateJWTToken(String secretKey) throws RuntimeException {
  /**
   * Generates a JWT Token as accepted by a service like Zoom. Adjust the header and payload to fit the
   * service you are interacting with. Be sure to account for all spaces in header/payload! Also token string
   * is without padding. If you need padding, be sure to remove "withoutPadding()" calls.
   * @param  secretKey  Secret key used during encoding.
   * @return returns JWT token string based on header, payload and secretKey
   */
   String header = "{\"typ\":\"JWT\",\"alg\":\"HS256\"}"
   String base64UrlHeader = Base64.getUrlEncoder().withoutPadding().encodeToString(header.getBytes())

   // JWT token expires 60 seconds from now
   long timeSecs = (System.currentTimeMillis() / 1000) + 60

   String payload = "{\"iss\":\"${zoom_api_key}\",\"exp\":" + String.valueOf(timeSecs) + "}"
   String base64UrlPayload = Base64.getUrlEncoder().withoutPadding().encodeToString(payload.getBytes())

   try {
      String base64UrlSignature = hmacEncode(base64UrlHeader + "." + base64UrlPayload, secretKey)

      return base64UrlHeader + "." + base64UrlPayload + "." + base64UrlSignature
   } catch (Exception e) {
      throw new RuntimeException("Unable to generate a JWT token.")
   }
}

private String hmacEncode(String data, String key) throws Exception {
  /**
   * Helper method that encodes data using HmacSHA256 and key.
   * @param  data data to encode
   * @param  key  Secret key used during encoding.
   * @return Base64UrlEncoded string without padding
   */
   Mac sha256_HMAC = Mac.getInstance("HmacSHA256")
   SecretKeySpec secret_key = new SecretKeySpec(key.getBytes(), "HmacSHA256")
   sha256_HMAC.init(secret_key)

   return Base64.getUrlEncoder().withoutPadding().encodeToString(sha256_HMAC.doFinal(data.getBytes()))
}