import groovy.json.JsonSlurper

hostname = hostProps.get("system.hostname")

url = "https://${hostname}/v1/instances/status"

try {
    def payload = url.toURL().getText()
    // println(payload);println("=".multiply(80))
    def instances = new JsonSlurper().parseText(payload)

    //instances = instances.take(3)
    instances.each {
      println "${it.key}##${it.key}######environment=${it.environment}&location=${it.location}&isActive=${it.isActive}"
    }
    return 0
}
catch (Exception e) {
    println(e);return 1
}
