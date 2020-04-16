import com.santaba.agent.groovyapi.win32.WMI

def host = hostProps.get("system.hostname")

def service_list = WMI.queryAll(host, "select * from win32_Service WHERE STARTMODE = \"AUTO\"")

service_list.each {
  wildvalue = it["NAME"].replaceAll(/\=|\:|\\|\#|\s/, '')
  wildalias = it["DISPLAYNAME"]
  description = null
  //description = it["CAPTION"]  //uncomment this line to use the caption as the description (unlikely)
  caption = it["DESCRIPTION"]
  runasuser = it["STARTNAME"]
  path = it["PATHNAME"]
    println("${wildvalue}##${wildalias}##${description ?: ""}####caption=${caption}&runasuser=${runasuser}&path=${path}")
}

return(0)
