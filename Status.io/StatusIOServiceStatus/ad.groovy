import groovy.json.JsonSlurper

def statusIoKey = hostProps.get("statusio_key") ?: hostProps.get("auto.statusio_key")
def statusIoDomain = hostProps.get("statusio_domain") ?: "statuspage.io"

url = "https://${statusIoKey}.${statusIoDomain}/api/v2/summary.json"

def payload = url.toURL().getText()
def status = new JsonSlurper().parseText(payload)

status.components.each { component ->
    println "${component.id}##${component.name}"
}

return 0
