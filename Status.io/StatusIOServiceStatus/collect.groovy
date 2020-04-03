/*******************************************************************************
 * © 2007-2020 - LogicMonitor, Inc. All rights reserved.
 ******************************************************************************/


import groovy.json.JsonSlurper

def statusIoKey = hostProps.get("statusio_key") ?: hostProps.get("auto.statusio_key")
def statusIoDomain = hostProps.get("statusio_domain") ?: "statuspage.io"

url = "https://${statusIoKey}.${statusIoDomain}/api/v2/summary.json"

def STATUS_MAP = ["operational":0, "degraded_performance": 1, "partial_outage": 2, "major_outage": 3]

def payload = url.toURL().getText()
def status = new JsonSlurper().parseText(payload)

status.components.each { component ->
    println "${component.id}.status=${STATUS_MAP.get(component.status, component.status)}"
}

return 0