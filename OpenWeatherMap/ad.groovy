hostProps.get("weather.locations").tokenize("|").each{
    location = it.tokenize("!")
    println("${location[1].trim()}${(location[2] ?: "us").trim()}##${location[0].trim()}")
}
return 0