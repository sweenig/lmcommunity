import com.jcraft.jsch.JSch
import com.santaba.agent.util.Settings
host = hostProps.get("system.hostname")
user = hostProps.get("ssh.user")
pass = hostProps.get("ssh.pass")
port = hostProps.get("ssh.port") ?: 22
cert = hostProps.get("ssh.cert") ?: '~/.ssh/id_rsa'
timeout = 15000 // timeout in milliseconds
try {
  def output = getCommandOutput('ps aux').readLines()
  output.subList(2,output.size()-2).each{line ->
    e = line.tokenize(" ")
    println("${e[1]}.cpu: ${e[2]}")
    println("${e[1]}.mem: ${e[3]}")
    println("${e[1]}.vsz: ${e[4]}")
    println("${e[1]}.rss: ${e[5]}")
  }
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
  catch (Exception e) {e.printStackTrace()}
  finally {session.disconnect()}
}