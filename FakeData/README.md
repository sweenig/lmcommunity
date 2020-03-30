# Generates fake data for display in LogicMonitor

## Bell_Curves
This was a first attempt at a datasource that generated better-than-junk data. We needed a way to display data that looked more realistic than current options.
* bell - simply generates a bell curve based on the time of day, centered around noon(ish).
* lmlogo - an accidental discovery, this datapoint uses the time of day and some complex aliasing to generate something that looks an awful lot like the old LogicMonitor logo. To be honest, this datapoint is the only reason I keep this DS around. It's fun to have the LM logo plotted on a graph on a welcome dashboard. I think I scale the value up by adding 4000 so that it clears the x-axis.

![Old LM Logo](Bell_Curves/old_lm_logo.png)

## Sinusoids
This was the second attempt at generating fake data that looked more realistic. Once the LM logo fell out of the above DS, I decided it was a good time to fork to this one.

This DS replicates what a single instance DS would look like. The data generally grows over the course of the day then goes back down.

![Sinusoids, single instance](Sinusoids/sinusoids.png)

You can set the following properties to manipulate the data somewhat:
* sine.timeshift: should shift left or right so that you can make the max point of the hump happen at any time you want.
* sine.scale: should shift the number larger or smaller in the y direction.
* sine.period: number of seconds before repeating (defaults to 1440, or one day)

## Sinusoids v2
This was my final attempt at making some fake data before switching to a better method of replaying real, sanitized data (can't get more real than real data replayed).
This one allows you to add as many instances as you want. Each instance can have the same properties as the previous version:
* sine.timeshift: should shift left or right so that you can make the max point of the hump happen at any time you want.
* sine.scale: should shift the number larger or smaller in the y direction.
* sine.period: number of seconds before repeating (defaults to 1440, or one day)

This time, set the properties on the instances after you add them through "Add additional monitoring". One additional property, `sine.addlpoints` allows you to specify the number of datapoints to return per instance (up to 10). Semi-random values will be generated for the other points.
This is what some instances could be:

![Instances](Sinusoids%20v2/instances.png)

This is what it would look like if you just added one instance:

![Standard](Sinusoids%20v2/standard.png)

This is what it would look like if you added an instance and only time shifted it.

![Time Shifted](Sinusoids%20v2/time_shifted.png)

This is what it would look like if you added an instance and adjusted the period.

![Shorter Period](Sinusoids%20v2/shorter_period.png)

This is what it would look like if you added an instance and adjusted the hight scale.

![Scaled Height](Sinusoids%20v2/scaledheight.png)

This is what it would look like if you added an instance and gave it more datapoints to output.

![Multiple Points per Instances](Sinusoids%20v2/multiplepoints.png)

This is what it would look like if you added an instances and modified all the parameters from the defaults:

![Everything customized](Sinusoids%20v2/all_custom.png)]
