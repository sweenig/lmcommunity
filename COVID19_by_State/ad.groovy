import groovy.json.JsonSlurper
jsondata = new URL("https://finnhub.io/api/v1/covid19/us?token=${hostProps.get('finnhub.api.key')}").getText()
objectdata = new JsonSlurper().parseText(jsondata)
countries = [
    canada: ["Alberta","British Columbia","Manitoba","New Brunswick","Newfoundland and Labrador","Northwest Territories","Nova Scotia","Nunavut","Ontario","Prince Edward Island","Quebec","Saskatchewan","Yukon"],
    ships: ["Diamond Princess", "Grand Princess","Wuhan Evacuee"]
]

objectdata.each{
  state = it.state.trim()
  if (countries.canada.contains(state)) {country = "Canada"}
  else if (countries.ships.contains(state)) {country = "Other"}
  else country = "US"
  if (state.size() > 0){println("${state.replaceAll(/[\s,\.]/,"")}##${state}######country=${country}")}
}
return 0
