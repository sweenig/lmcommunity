Oid = "1.3.6.1.2.1.2.2.1" //polling the interfaces table (returns "metricOID.wildvalue = datavalue")
wildvalueTerms = 1

import com.santaba.agent.groovyapi.snmp.Snmp

def host = hostProps.get('system.hostname')
def props = hostProps.toProperties()
int timeout = 10000 // 10 sec timeout.

def snmpMapToTable(snmpmap, int wildvalueTerms = 1) {
    //println("Raw result of snmpwalk of ${Oid}:\n${snmpmap}\n${"=".multiply(80)}")
    rows = [:]
    snmpmap.each {k,v ->
        splits = k.tokenize(".")
        col = splits.dropRight(wildvalueTerms).join(".")
        wildvalue = splits.takeRight(wildvalueTerms).join(".")
        if (!(rows.containsKey(wildvalue))) { rows[wildvalue] = [:] }
        rows[wildvalue][col] = v
    }
    return rows
}

walkResult = Snmp.walkAsMap(host, Oid, props, timeout)
entryRaw = snmpMapToTable(walkResult, wildvalueTerms)

adminUpPortCount = 0
adminDownPortCount = 0
operUpPortCount = 0
operDownPortCount = 0
upup = 0
updown = 0
downup = 0
downdown = 0


entryRaw.each {k,v->
  // println("${k}: ${v["7"]} - ${v["8"]}")
  admin = v["7"]
  oper = v["8"]

  if (admin == "1") {adminUpPortCount += 1}
  else {adminDownPortCount += 0}

  if (oper == "1") {operUpPortCount +=1}
  else {operDownPortCount += 1}

  if (admin == "1") {
    if (oper == "1") {upup += 1}
    else {updown += 1}
  } else {
    if (oper == "1") {downup += 1}
    else {downdown += 1}
  }
}

println("adminUpPortCount: ${adminUpPortCount}")
println("adminDownPortCount: ${adminDownPortCount}")
println("operUpPortCount: ${operUpPortCount}")
println("operDownPortCount: ${operDownPortCount}")
println("totalPortCount: ${entryRaw.size()}")
println("upup: ${upup}")
println("updown: ${updown}")
println("downup: ${downup}")
println("downdown: ${downdown}")

return 0