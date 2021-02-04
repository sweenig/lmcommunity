import groovy.json.JsonOutput
hostname = hostProps.get("system.displayName")
data = [
    "rawERIs":[
        [
            "category":"net.l2",
            "priority":2,
            "type":"API",
            "value":hostname
        ]
    ]
]
println("rawERIs=" + JsonOutput.toJson(data))
return 0