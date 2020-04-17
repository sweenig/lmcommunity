import com.santaba.agent.groovyapi.win32.WMI

def host = hostProps.get("system.hostname")

def process_list = WMI.queryAll(host, "select * from Win32_PerfRawData_PerfProc_Process")

process_list.each{
  wildvalue=it["NAME"].replaceAll(/\=|\:|\\|\#|\s/, '')
  println wildvalue+".HandleCount="+it["HANDLECOUNT"]
  println wildvalue+".IODataBytesPerSec="+it["IODATABYTESPERSEC"]
  println wildvalue+".PercentProcessorTime="+it["PERCENTPROCESSORTIME"]
  println wildvalue+".ProcessID="+it["IDPROCESS"]
  println wildvalue+".ThreadCount="+it["THREADCOUNT"]
  println wildvalue+".WorkingSet="+it["WORKINGSET"]
}
return(0)