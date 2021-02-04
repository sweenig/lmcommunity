# LMCommUserStats

This DataSource provides the ability to fetch and report on the user statistics of particular users in any community run on the Invision platform. In this case, the community URL is hard coded into the script, but that can be modified by changing the `httpClient = HTTP.open("communityURL",443)` and `url` lines.

## Installation

Use the [standard methods](https://www.logicmonitor.com/support/rest-api-developers-guide/v1/datasources/import-datasources-from-xml) for importing the XML into LogicMonitor.

## Usage

Add a resource into LogicMonitor and give it the following properties:
- `lmcomm.key` - the API token for accessing the community
- `lmcomm.id` - a comma, space, or pipe separated list of user IDs to monitor. This property could be built by a PropertySource, but in our case, we have too many users to discover and track all of them, so we set the property manually.

You can clone the DS and change the Instance Discovery filter to include or exclude certain email domains or user groups. As a bonus, each user property pulls back the profile pic URL for that user.

The resulting data can be put into dashboards showing leaderboards for days since registration, time since last activity, time since last visit, time since last post, reputation points, post count, and profile views.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
