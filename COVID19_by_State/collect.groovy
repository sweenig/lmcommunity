import groovy.json.JsonSlurper
jsondata = new URL("https://finnhub.io/api/v1/covid19/us?token=${hostProps.get('finnhub.api.key')}").getText()
objectdata = new JsonSlurper().parseText(jsondata)
objectdata.each{
  state = it.state.trim()
  if (state.size() > 0){
    println("${state.replaceAll(/[\s,\.]/,"")}.deaths: ${it.death}")
    println("${state.replaceAll(/[\s,\.]/,"")}.case: ${it.case}")
  }
}
return 0