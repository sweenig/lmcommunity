hostProps.get("Service_restart.services").tokenize(",|").each{
    println("${it}##${it}")
}
return 0