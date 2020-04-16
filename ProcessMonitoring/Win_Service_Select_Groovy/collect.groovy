import com.santaba.agent.groovyapi.win32.WMI

def host = hostProps.get("system.hostname")

def service_list = WMI.queryAll(host, "select * from win32_Service WHERE STARTMODE = \"AUTO\"")

//Enumerations obtained from https://docs.microsoft.com/en-us/windows/win32/cimwin32prov/win32-service and put in my preferred order so that they are in ascending severity. This allows thresholds for >= 1 3 5.
stateEnum = [
  "Running",
  "Start Pending",
  "Stop Pending",
  "Continue Pending",
  "Pause Pending",
  "Stopped",
  "Paused",
  "Unknown"
]

statusEnum = [
  "OK",
  "Error",
  "Degraded",
  "Unknown",
  "Pred Fail",
  "Starting",
  "Stopping",
  "Service",
  "Stressed",
  "NonRecover",
  "No Contact",
  "Lost Comm"
]

service_list.each{
  wildvalue = it["NAME"].replaceAll(/\=|\:|\\|\#|\s/, '')
  println("${wildvalue}.state: ${stateEnum.indexOf(it["STATE"])}")
  println("${wildvalue}.status: ${statusEnum.indexOf(it["STATUS"])}")
}
return(0)