import groovy.json.JsonSlurper

def statusIoKey = hostProps.get("statusio_key") ?: hostProps.get("auto.statusio_key")
def statusIoDomain = hostProps.get("statusio_domain") ?: "statuspage.io"

url = "https://${statusIoKey}.${statusIoDomain}/api/v2/summary.json"

def payload = url.toURL().getText()
// println(payload);println("=".multiply(80))
def status = new JsonSlurper().parseText(payload)

status.components.each { component ->
  if (component.group == true) {
    group = "group=" + component.name
  } else {
    if (component.group_id){
      group = "group=" + status.components.find{it.id == component.group_id}.name
    } else {
      group = ""
    }
  }
    println "${component.id}##${component.name}######${group}"
}

return 0


// import groovy.json.*

// def statusIoKey = hostProps.get("statusio_key") ?: hostProps.get("auto.statusio_key")

// url = "https://${statusIoKey}.statuspage.io/api/v2/summary.json"
// def status = new JsonSlurper().parseText(url.toURL().getText())
// easy_map = [:]
//
// status.components.each { component->
//     if(component.group == false) {easy_map[component.id] = component}
// }
//
// status.components.each {group->
//     if(group.group == true) {
//         group.components.each { sub_component ->
//             group_component = group.name.replace(" ","_") + "_" + easy_map[sub_component]['name'].replace(" ","_")
//             println group_component + "##" + easy_map[sub_component]['name'] + " - " + group.name + "######auto.status_group=${group.name}"
//         }
//     } else if(group.group_id == null) {
//         println group.name.replace(" ","_") + "##" + group.name
//     }
// }
// return 0
