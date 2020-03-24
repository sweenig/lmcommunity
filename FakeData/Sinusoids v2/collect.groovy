timeshift = (instanceProps.get("sine.timeshift") ?: -450).toInteger()
scale = (instanceProps.get("sine.scale") ?: 1).toInteger()
period = (instanceProps.get("sine.period") ?: 1440).toInteger()
n = Math.min((instanceProps.get("sine.addlpoints") ?: 0).toInteger(),10)
sinusoids = [
    [0.5,1,0],
    [1,1/2,0],
    [2,1/4,0],
    [4,1/8,0],
    [8,1/16,0],
    [16,1/32,0],
    [1,1/2,Math.PI/2]
]
origin_date = new Date(119,0,0,0,0,0) //01JAN2019 00:00:00 doesn't matter the date as long as it's midnight
current_date = new Date()

use(groovy.time.TimeCategory) {
    duration = current_date - origin_date
    x = duration.hours * 60 + duration.minutes
    θ = (x + timeshift) / period * 2 * Math.PI
}

datapoints = [0] * n
//datapoints = [0,0,0,0,0]
datapoints.eachWithIndex { v, i ->
    y = 0
    sinusoids.each { harmonic, impact, phase_shift ->
        y += impact * Math.sin(harmonic * (θ + phase_shift))
    }
    rand_scale = new Random().nextInt(50)
    datapoints[i] = y * rand_scale * 10
}

y = 0
sinusoids.each { harmonic, impact, phase_shift ->
    y += impact * Math.sin(harmonic * (θ + phase_shift))
}


println("""x: ${x}
θ: ${θ}
y: ${y}
Timeshift: ${timeshift}
Scale: ${scale}
Period: ${period}""")
datapoints.eachWithIndex { v, i -> println("y${i}: ${v}")}
return 0