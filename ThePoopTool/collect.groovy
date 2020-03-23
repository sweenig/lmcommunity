stashdateraw = hostProps.get("stash.date")
stashcount = hostProps.get("stash.count").toInteger()
stashpeople = hostProps.get("stash.people").toInteger()

stashwilllast = 12 * stashcount / stashpeople
def stashdate = Date.parse("MM/dd/yyyy",stashdateraw)
def now = new Date()
stashage = now - stashdate
stashremaining = stashwilllast - stashage
println(stashremaining)


return 0