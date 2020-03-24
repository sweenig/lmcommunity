import com.santaba.agent.groovyapi.http.*
println(new URL("https://www.treasurydirect.gov/NP_WS/debt/current?format=json").getText())
return 0