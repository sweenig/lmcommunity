page = new URL("https://oilprice.com/oil-price-charts").getText()
// println(page + "\n" + "=".multiply(80))
ad = false
instances = [
  "WTI Crude":    /<td>WTI Crude.*\s*<td class='last_price' data-price='(.*?)'>.*<.td><td dir='ltr' class='change_/,
  "Brent Crude":/<td>Brent Crude.*\s*<td class='last_price' data-price='(.*?)'>.*<.td><td dir='ltr' class='change_/,
]
instances.each {k,v ->
  if (ad){
    println("${k.replaceAll(" ","")}##${k}")
  } else {
    if ((page =~ v).size() > 0){ //this might be doable with elvis, but this works
      println("${k.replaceAll(" ","")}.price: ${(page =~ v)[0][1]}")
    }
  }
}

return 0