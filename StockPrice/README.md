# Stock Price Tracker

Very simple DS that tracks the status of stocks of your choosing. An API key from Finnhub.io is required to run this DataSource. Just sign up for a free account and grab the API key from your account page. Store it as a property on whichever resource you want the data applied to with property name `finnhub.api.key`.

Once you've got that working, you will need to store the ticker symbol(s) as a pipe, space, or comma separated list in a property called `stocks`.

You'll need to keep Finnhub's rate limit in consideration. They only allow 60 API calls per 60 seconds. Meaning that you will only be able to track a maximum of 60 ticker symbols, probably practically a few less. Even changing the poll rate to 2, 3, 5, or more minutes won't help because when polling happens, it polls once for each ticker symbol.
