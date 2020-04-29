import groovy.json.JsonOutput
import groovy.json.JsonSlurper
import org.apache.commons.codec.binary.Hex
import org.apache.http.client.methods.*
import org.apache.http.entity.ContentType
import org.apache.http.entity.StringEntity
import org.apache.http.impl.client.CloseableHttpClient
import org.apache.http.impl.client.HttpClients
import org.apache.http.util.EntityUtils
import javax.crypto.Mac
import javax.crypto.spec.SecretKeySpec
import java.net.URLEncoder

ip = hostProps.get("system.hostname")
userid = hostProps.get("ssh.user")
password = hostProps.get("ssh.pass")

accessId = hostProps.get("paloalto.apikey.lm.id")
accessKey = hostProps.get("paloalto.apikey.lm.key")
company = hostProps.get("paloalto.apikey.lm.company")

if (!accessId || !accessKey || !company){
  println("LM API credentials missing.")
  println("ID: ${accessId}\nKey: ${accessKey.replaceAll(/./,"*")}\nCompany: ${company}")
  return 1
}

devId = hostProps.get("system.deviceId")
existingkey = hostProps.get("paloalto.apikey.pass")
// println("Existing key: ${existingkey}")
encodedPassword = URLEncoder.encode(password, "UTF-8")

// get key from api
pageXML = new URL("https://${ip}/api/?type=keygen&user=${userid}&password=${encodedPassword}").getText().trim().replaceAll(/\n/,"").replaceAll(" ","")
// pageXML = """
// <response status="success">
//   <result>
//     <key>
//       KEY_HERE
//     </key>
//   </result>
// </response>
// """.trim().replaceAll(/\n/,"").replaceAll(" ","")
key = (pageXML =~ /<key>(.*)<\/key>/)[0][1]
// println("New key: ${key}")

if (existingkey != key){ //new key is different than existing key
  if (existingkey) { //property already exists, put it
    println("Property exists. Updating it...")
    data = JsonOutput.toJson(["value":key])
    response = LMAPI("PUT",accessId,accessKey,company,"/device/devices/${devId}/properties/paloalto.apikey.pass/","",data)
  } else { //property does not exist, post it
    println("Property does not exist. Creating it...")
    data = JsonOutput.toJson(["name":"paloalto.apikey.pass","value":key])
    response = LMAPI("POST",accessId,accessKey,company,"/device/devices/${devId}/properties/","",data)
  }
  println("Response code- ${response?.code}\nResponse body- ${response?.body}")
} else {println("New key matches existing key. Nothing to do.")}

return 0

def LMAPI(String _verb, _accessId, _accessKey, _account, GString _resourcePath, String _queryParameters, String _data){
  responseDict = [:]
  url = 'https://' + _account + '.logicmonitor.com' + '/santaba/rest' + _resourcePath + _queryParameters
  StringEntity params = new StringEntity(_data, ContentType.APPLICATION_JSON)
  epoch = System.currentTimeMillis()
  requestVars = _verb + epoch + _data + _resourcePath
  hmac = Mac.getInstance('HmacSHA256')
  secret = new SecretKeySpec(_accessKey.getBytes(), 'HmacSHA256')
  hmac.init(secret)
  hmac_signed = Hex.encodeHexString(hmac.doFinal(requestVars.getBytes()))
  signature = hmac_signed.bytes.encodeBase64()
  CloseableHttpClient httpclient = HttpClients.createDefault()
  if (_verb == 'PUT'){
      http_request = new HttpPut(url)
  } else if (_verb == 'POST'){
      http_request = new HttpPost(url)
  } else{println('INVALID HTTP VERB')}
  http_request.addHeader("Authorization", "LMv1 " + _accessId + ":" + signature + ":" + epoch)
  http_request.setHeader("X-Version", "2")
  http_request.setHeader("Accept", "application/json")
  http_request.setHeader("Content-type", "application/json")
  http_request.setEntity(params)
  response = httpclient.execute(http_request)
  responseBody = EntityUtils.toString(response.getEntity())
  code = response.getStatusLine().getStatusCode()
  responseDict['code'] = code ?: null
  responseDict['body'] = responseBody ?: null
  return responseDict
}
