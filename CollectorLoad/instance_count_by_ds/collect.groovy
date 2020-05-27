//initialize
import javax.crypto.Mac
import javax.crypto.spec.SecretKeySpec
import org.apache.commons.codec.binary.Hex
import groovy.json.JsonSlurper

def generate_headers(id, key, path) {
  try {
    // Create encryption signature for authorization request
    Long epoch_time = System.currentTimeMillis()  // Get current system time (epoch time)
    Mac hmac = Mac.getInstance("HmacSHA256")
    hmac.init(new SecretKeySpec(key.getBytes(), "HmacSHA256"))
    signature = Hex.encodeHexString(hmac.doFinal("GET${epoch_time}${path}".getBytes())).bytes.encodeBase64()
    // return headers to main function
    return ["Authorization": "LMv1 $id:$signature:$epoch_time", "Content-Type": "application/json"]
  } catch (Exception err) {
    // If error occurred, print the error message
    println("ERROR: Unable to establish encryption for $path. Attempting next resource...\n${err.message}")
  }
}

def get_response(resource, parameters, account, headers) {
  try {
    boolean proceed = true  // Boolean used to determine if additional pagination is required
    // Map to store query results for each endpoint.  Contains a list to store actual returned values and a boolean to determine if successful
    Map results = ["response": [],
             "success" : true]
    add_query_parameters(resource, parameters)
    // Add initial offset and size values to appropriate categories (skips metrics category since it's stagnate)
    while (proceed) {
      // Used for paginating through all availabe results.  Grabs 1000 at a time and moves offset if another query is required.
      Map query = query_resource(account, parameters, headers)
      // Query each API endpoint for a response (Should receive as Map)
      // If the response was successful (including status and error messages), proceed to printing results
      if (query && query?.data && query?.status == 200 && query?.errmsg?.toUpperCase() == "OK") {
        if (resource != "metrics") {
          results.response.addAll(query.data.items)   // Add all the data items found to our results map data list
          if (query?.data?.items?.size() < parameters.details.size) {
            // If we received less than 1000 results
            proceed = false   // There is no need to execute another API query with a shifted offset
          } else {    // Otherwise
            parameters.details.offset += parameters.details.size
            // Shift the offset to start 1000 numbers from current position
          }
        } else {
          results.response = query.data   // Add all the data items found to our results map data list
          proceed = false   // We've successfully queried all values.  End while loop
        }
      } else {
        // If response was not successful, print eror message for each category that failed and continue to next endpoint
        // If response error and status can be determined, print them.  Otherwise, use UNKNOWN
        println("ERROR: Failed to query $resource API Endpoint...\n" +
            "${query?.errmsg?.toUpperCase() ?: 'UNKNOWN'} (STATUS: ${query?.status ?: 'UNKNOWN'})")
        results.success = false   // Set success value to false since we failed our API query
        proceed = false   // End while loop because of failure and proceed to next endpoint
      }
    }
    return results  // Return results to main function
  } catch (Exception err) {
    println("ERROR: Script failed while attempting to query $resource API endpoint...\n${err?.message}")
  }
}

def add_query_parameters(category, parameters) {
  // Add size and offset field to map (only if collectors or admins category)
  if (category != "metrics") {
    Map query_details = ["size"  : 1000, "offset": 0]
    // If there's already a details key in the details map
    if (parameters.details) {
      parameters.details << query_details
      // Append the query details information to the pre-existing details map
    } else {  // Otherwise, create a details key and assign it the query details map as a value
      parameters.put("details", query_details)
    }
  }
}

def query_resource(account, details, headers) {
  try {
    // Configure request url from account, path, and authorization headers
    String url = "https://${account}.logicmonitor.com/santaba/rest${details.path}?${pack_parameters(details.details)}"
    // Return query response, converted from JSON to usable map
    return new JsonSlurper().parseText(url.toURL().getText(useCaches: true, allowUserInteraction: false, requestProperties: headers))
  } catch (Exception err) { // If error occurred, print the error message
    println("ERROR: Unable to query ${details.path} for details.\n${err.message}")
  }
}

def pack_parameters(query_details) { // If additional query details are located in map, include them in url string
  List pairs = []
  query_details?.each { k, v -> pairs.add("${k}=${v}")}
  return pairs.join("&")
}

//setup
ds_name = "instance_count_by_ds"
Map credentials = [
  "id"   : hostProps.get("${ds_name}.id"),
  "key"  : hostProps.get("${ds_name}.pass"),
  "account": hostProps.get("${ds_name}.account")
]

deviceid = hostProps.get("system.deviceId")

Map resources = [:]
resources["instances"] = ["path": "/device/devices/${deviceid}/instances", "details": ["fields": "name"]]

//gather
if (credentials.account && credentials.id && credentials.key) {
  resources.each() { k, v ->
    Map headers = generate_headers(credentials.id, credentials.key, v.path)
    if (headers) {
      Map response = get_response(k, v, credentials.account, headers)
      if (response?.success) {resources[k]["data"] = response.response}
    }
  }
} else {
  println("""Device is not configured with the necessary portal credentials to proceed with API queries.
Please ensure that \"${ds_name}.id\", \"${ds_name}.pass\", and \"${ds_name}.account\" are set in the collector properties section!
Exiting Program...""")
  return 1
}

dscounts = [:]

//transform
resources.instances.data.each(){
  dsname = it.name.tokenize("-")[0].replaceAll(" ","")
  if (dscounts.containsKey(dsname)) {
    dscounts[dsname] += 1
  } else {
    dscounts[dsname] = 1
  }
}

//output
collect = true
dscounts.each{k,v->
  if (collect) {
    println("${k}.count: ${v}")
  } else {
    println("${k}##${k}")
  }
}

return 0