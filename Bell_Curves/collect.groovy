bell_center = 719.5
bell_narrowness = 200
bell_height = 10000
noise_level = 3
noisiness = 0.1
y_shift = 2
currtime = new Date().format('HH:mm').tokenize(":")
minutes_since_midnight = currtime[0].toInteger()*60 + currtime[1].toInteger()
x = minutes_since_midnight

bell_curve = ((bell_height/(bell_narrowness * Math.sqrt(2*Math.PI))* Math.exp(-1*((x-bell_center)**2)/(2*bell_narrowness**2)))+y_shift)**2

high_freq_noise = Math.sin(x * noisiness * 2)
low_freq_noise = Math.sin(x * noisiness / 4)
noise_component = noise_level * (high_freq_noise + low_freq_noise) * bell_curve
//=($K$2/($I$2*(SQRT(2*pi())))*exp(-1*((B4-$J$2)^2)/(2*$I$2^2))+$O$2)
bell_component = (bell_height/(bell_narrowness*(Math.sqrt(2*Math.PI)))*Math.exp(-1*((x-bell_center)**2)/(2*bell_narrowness**2))+y_shift)

println("""bell_curve: ${bell_curve}
lm_logo: ${noise_component + bell_component}
""")
return 0