import groovy.json.JsonSlurper
stocks = hostProps.get("stocks").tokenize(",| ")
token = hostProps.get("finnhub.api.key")
stocks.each{
  try {
    url = "https://finnhub.io/api/v1/quote?token=${token}&symbol=${it}"
    jsondata = url.toURL().getText()
    data = new JsonSlurper().parseText(jsondata)
    data.each{k,v-> println("${it}.${k}: ${v}")}
  } catch (Exception e) {println(e);return 1}
}
return 0