import com.santaba.agent.groovyapi.win32.WMI

def host = hostProps.get("system.hostname")

def process_list = WMI.queryAll(host, "select * from Win32_PerfRawData_PerfProc_Process")

process_list.each {
  println("${it["NAME"].replaceAll(/\=|\:|\\|\#|\s/, '')}##${it["NAME"]}")
}
return(0)
