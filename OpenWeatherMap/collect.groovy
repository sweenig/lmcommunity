import groovy.json.JsonSlurper

key = hostProps.get("openweather.key")

fromJson = new JsonSlurper()

hostProps.get("weather.locations").tokenize("|").collect{[it.tokenize("!")[1].trim(),(it.tokenize("!")[2] ?: "us").trim()]}.each{ wildvalue,country ->
    url = "https://api.openweathermap.org/data/2.5/weather?zip=${wildvalue},${country}&appid=${key}"
    try {
        payload = url.toURL().getText()
        data = fromJson.parseText(payload)
        println(wildvalue + country + ".code: " + data.cod)
        println(wildvalue + country + ".feels_like: " + data.main.feels_like) //in kelvin
        println(wildvalue + country + ".humidity: " + data.main.humidity)
        println(wildvalue + country + ".pressure: " + data.main.pressure)
        println(wildvalue + country + ".temp: " + data.main.temp) //in kelvin
        println(wildvalue + country + ".temp_max: " + data.main.temp_max) //in kelvin
        println(wildvalue + country + ".temp_min: " + data.main.temp_min) //in kelvin
        println(wildvalue + country + ".wind_speed: " + data.wind.speed)
        println(wildvalue + country + ".wind_degrees: " + data.wind.deg)
        println(wildvalue + country + ".cloudiness: " + data.clouds.all)
    } catch (Exception e) { 
        println(wildvalue + country + ".code: 404")
    }
}

return 0