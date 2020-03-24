/*******************************************************************************
 *  © 2007-2019 - LogicMonitor, Inc. All rights reserved.
 ******************************************************************************/
import org.apache.http.client.methods.HttpGet
import org.apache.http.impl.client.CloseableHttpClient
import org.apache.http.impl.client.HttpClients
import org.apache.http.util.EntityUtils
import javax.crypto.Mac
import javax.crypto.spec.SecretKeySpec
import org.apache.commons.codec.binary.Hex
import groovy.json.JsonSlurper

CLIENTS_FOLDER_NAME = hostProps.get("billing_api.client_path") ?: "Fred Hutchinson Devices by Location"
BILLING_TYPES_PARENT_FOLDER_NAME = hostProps.get("billing_api.types_parent_path") ?: "Devices by Billing Type"

accessId = hostProps.get("billing_api.id")
accessKey = hostProps.get("billing_api.pass")
account = hostProps.get("billing_api.account")
queryLimit = hostProps.get("billing_api.query_limit") ? hostProps.get("billing_api.query_limit").toInteger() : 1000

s = new JsonSlurper()

def LMAPI(_verb, _accessId, _accessKey, _account, _resourcePath, _queryParameters = [:], _data = '') {
    url = 'https://' + _account + '.logicmonitor.com' + '/santaba/rest/' + _resourcePath
    if (_queryParameters.size() > 0) {
        _encodedQueryParameters = []
        _queryParameters.each{k,v ->
            _encodedQueryParameters += "${k}=${java.net.URLEncoder.encode(v)}"
        }
        url += "?" + _encodedQueryParameters.join("&")
    } else {url += "/"}
    epoch = System.currentTimeMillis()
    requestVars = _verb + epoch + "/" + _resourcePath
    hmac = Mac.getInstance('HmacSHA256')
    secret = new SecretKeySpec(_accessKey.getBytes(), 'HmacSHA256')
    hmac.init(secret)
    hmac_signed = Hex.encodeHexString(hmac.doFinal(requestVars.getBytes()))
    signature = hmac_signed.bytes.encodeBase64()
    CloseableHttpClient myHttpClient = HttpClients.createDefault()
    http_request = new HttpGet(url)
    http_request.addHeader("Authorization" , "LMv1 " + _accessId + ":" + signature + ":" + epoch)
    http_request.setHeader("X-Version", "2")
    response = myHttpClient.execute(http_request)
    responseBody = EntityUtils.toString(response.getEntity())
    code = response.getStatusLine().getStatusCode()
    myHttpClient.close()
    responseDict = [:]
    responseDict['code'] = code ?: null
    responseDict['body'] = responseBody ?: null
    return responseDict
}

def LmGet(String _resourcePath, Map _queryParameters = [:]){return LMAPI("GET", accessId, accessKey, account, _resourcePath, _queryParameters)}

queryParameters = [
'fields':'groupType,fullPath,id,numOfHosts,parentId,numOfAWSDevices,numOfAzureDevices,numOfDirectDevices,numOfDirectSubGroups,numOfGcpDevices',
'sort':'+fullPath',
'size':queryLimit.toString()
]
data_json = LmGet("device/groups",queryParameters)
data = s.parseText(data_json.body).items
data.each{
  path = it.fullPath.tokenize("/")
  println("${it.id}.numOfHosts: ${it.numOfHosts}")
  println("${it.id}.numOfAWSDevices: ${it.numOfAWSDevices}")
  println("${it.id}.numOfAzureDevices: ${it.numOfAzureDevices}")
  println("${it.id}.numOfDirectDevices: ${it.numOfDirectDevices}")
  println("${it.id}.numOfDirectSubGroups: ${it.numOfDirectSubGroups}")
  println("${it.id}.numOfGcpDevices: ${it.numOfGcpDevices}")
}

return 0