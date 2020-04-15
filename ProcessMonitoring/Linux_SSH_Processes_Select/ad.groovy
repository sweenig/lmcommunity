import com.jcraft.jsch.JSch
import com.santaba.agent.util.Settings
host = hostProps.get("system.hostname")
user = hostProps.get("ssh.user")
pass = hostProps.get("ssh.pass")
port = hostProps.get("ssh.port") ?: 22
cert = hostProps.get("ssh.cert") ?: '~/.ssh/id_rsa'
timeout = 15000 // timeout in milliseconds
try {
  def userCmd = getCommandOutput('ps ax -o pid,user,tty')
  users = userCmd.readLines().collectEntries{[it.tokenize(" ")[0], [it.tokenize(" ")[1],it.tokenize(" ")[2]]]}
  def processes = getCommandOutput('ps ax -o pid,command').readLines()
  processes.subList(2,processes.size()-2).each{
    e = it.tokenize(" ")
    pid = e[0]
    command = e[1..e.size()-1].join(" ")
    print("${pid}##[${pid}]${command}######")
    print("pid=${pid}")
    if (users[pid]){
      print("&tty=${users[pid][1]}")
      print("&user=${users[pid][0]}")
    } else {
      print("&user=UnknownUser")
    }
    print("\n")
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
