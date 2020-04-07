import com.santaba.agent.groovyapi.win32.WMI

def hostname = hostProps.get("system.hostname")

try {
  def namespace = "CIMv2";
  def timeout = 30;
  def wmi_query = 'select * from win32_serverconnection';
  def wmi_output_all = WMI.queryAll(hostname, namespace, wmi_query, timeout);
  def shareCounts = [:]
  wmi_output_all.each {
    if (shareCounts.containsKey(it["SHARENAME"])) {
      shareCounts[it["SHARENAME"]] += it["NUMBEROFUSERS"].toInteger()
    } else {
      shareCounts[it["SHARENAME"]] = it["NUMBEROFUSERS"].toInteger()
    }
  }

shareCounts.each{k,v -> println("${k}.numofusers: ${v}")}

return 0
} catch (Exception e) {println e;return 1}
