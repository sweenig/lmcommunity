import com.jcraft.jsch.JSch
import groovy.json.JsonSlurper
import com.santaba.agent.util.Settings

host = hostProps.get("system.hostname")
user = hostProps.get("ssh.user")
pass = hostProps.get("ssh.pass")
port = hostProps.get("ssh.port") ?: 22
cert = hostProps.get("ssh.cert") ?: '~/.ssh/id_rsa'
timeout = 15000 // timeout in milliseconds

pythonScript = """import json
from pijuice import PiJuice
x=PiJuice(1,0x14)
output = {}
output["charge"] = x.status.GetChargeLevel()
output["status"] = x.status.GetStatus()
output["temp"] = x.status.GetBatteryTemperature()
output["voltage"] = x.status.GetBatteryVoltage()
output["current"] = x.status.GetBatteryCurrent()
output["iovoltage"] = x.status.GetIoVoltage()
output["iocurrent"] = x.status.GetIoCurrent()
print(json.dumps(output))
"""

power_input_status = ["NOT_PRESENT": 0, "BAD": 1, "WEAK": 2, "PRESENT": 3]
battery_status = ["NORMAL": 0, "CHARGING_FROM_IN": 1, "CHARGING_FROM_5V_IO": 2, "NOT_PRESENT": 3]

try {
  def userCmd = getCommandOutput("python3 -c \"${pythonScript.replaceAll("\"","'").replaceAll("\n",";")}\"")
  data = new JsonSlurper().parseText(userCmd)
  println("5v_power_input_status: ${power_input_status[data.status.data.powerInput5vIo]}")
  println("charge: ${data.charge.data}")
  println("battery_status: ${battery_status[data.status.data.battery]}")
  println("power_input_status: ${power_input_status[data.status.data.powerInput]}")
  return 0
}
catch (Exception e) {println "Unexpected Exception : " + e; return 1}

def getCommandOutput(String input_command) {
  try {
    jsch = new JSch()
    if (user && !pass) {jsch.addIdentity(cert)}
    session = jsch.getSession(user, host, port)
    session.setConfig("StrictHostKeyChecking", "no")
    String authMethod = Settings.getSetting(Settings.SSH_PREFEREDAUTHENTICATION, Settings.DEFAULT_SSH_PREFEREDAUTHENTICATION)
    session.setConfig("PreferredAuthentications", authMethod)
    session.setTimeout(timeout)
    if (pass) {session.setPassword(pass)}
    session.connect()
    channel = session.openChannel("exec")
    channel.setCommand(input_command)
    def commandOutput = channel.getInputStream()
    channel.connect()
    def output = commandOutput.text
    channel.disconnect()
    return output
  }
  catch (Exception e) {e.printStackTrace();println("Error in SSH connection.")}
  finally {session.disconnect()}
}