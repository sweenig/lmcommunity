import groovy.json.JsonSlurper
stocks = hostProps.get("stocks").tokenize(",| ")
token = hostProps.get("finnhub.api.key")
stocks.each{
  try {
    url = "https://finnhub.io/api/v1/stock/profile?token=${token}&symbol=${it}"
    // println(url)
    jsondata = url.toURL().getText()
    data = new JsonSlurper().parseText(jsondata)
    // println(data)
    println("${it}##${data.name}##${data.weburl}####address=${data.address} ${data.city} ${data.state}&phone=${data.phone}&exchange=${data.exchange}&currency=${data.currency}")
  } catch (Exception e) {println(e);return 1}
}
return 0
