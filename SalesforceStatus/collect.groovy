import groovy.json.JsonSlurper

hostname = hostProps.get("system.hostname")

url = "https://${hostname}/v1/instances/status"

def STATUS_MAP = ["OK":0,"MAINTENANCE_CORE":1,"MAINTENANCE_NONCORE":1,"MINOR_INCIDENT_CORE":2,"MINOR_INCIDENT_NONCORE":2,"MAJOR_INCIDENT_CORE":3,"MAJOR_INCIDENT_NONCORE":3]

try {
  def payload = url.toURL().getText()
  def instances = new JsonSlurper().parseText(payload)
  //instances = instances.take(50)
  instances.each {
      println("${it.key}.status=${STATUS_MAP.get(it.status, it.status)}")
      println("${it.key}.incidentCount=${it.Incidents.size()}")
      println("${it.key}.maintCount=${it.Maintenances.size()}")
      println("${it.key}.productCount=${it.Products.size()}")
  }

  return 0
}
catch (Exception e) {
  println(e)
  return 1
}