This DataSource was written as a joke, but does work. It's based on the great website [The Poop Tool](https://thepooptool.com/), which calculates how many days a toilet paper stash will last given the current number of rolls and the number of people utilizing those rolls. 

In our case, you need to specify how many rolls you have on a given date, along with the number of people using it. You do this by adding "The Poop Tool|thepooptool.com" as a resource in your portal and adding the following properties:
* stash.date => the date the next property was accurate
* stash.count => the number of rolls you have
* stash.people => number of people using the stash

If you happen to purchase new rolls before you run out, you can just add the new rolls to the stash.count.  However, be sure to do this before the days remaining reaches zero. If you add it after it goes to zero, some of the rolls will go towards getting your days remaining back toward positive. Instead, you will want to reset the date along with the total count to whatever the current values are.

You might also find it handy to add an Ops Note whenever you make those changes to help visualize why your days remaining jumps up.
