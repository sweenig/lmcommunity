import groovy.json.JsonSlurper
stocks = hostProps.get("stocks").tokenize(",| ")
token = hostProps.get("finnhub.api.key")
url = "https://finnhub.io/api/v1/stock/symbol?exchange=US&token=${token}"
try {
  jsondata = url.toURL().getText()
  data = new JsonSlurper().parseText(jsondata)
  data.each{
     if (stocks.contains(it.symbol)) {println("${it.symbol}##${it.description}")}
  }
} catch (Exception e) {println(e);return 1}
return 0
