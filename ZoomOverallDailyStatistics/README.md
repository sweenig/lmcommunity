# Zoom Overall Daily Statistics

This datasource was originally written by Stefan Wuensch and uses the Zoom API to collect daily cumulative metrics: total meeting minutes since midnight, total meetings since midnight, new users, and participants.

The way the data is presented by the API isn't ideal because it doesn't give a current value. Instead, we fetch a report and look at the most recent value, which should represent today. That number is updated in the API between every 7-13 minutes. For this reason, we left the datapoint type as gauge instead of counter/derive. Setting the datapoint type to counter/derive would result in the data being 0 for any poll cycle where the value in the API hasn't been updated since the last poll, and it shows an enormous spike when it has been updated.

It also appears that the data continues to update even after the day has ended, so there's some issues there.

What I'm getting at is this: USE THIS AT YOUR OWN RISK. THE DATA MIGHT NOT MEAN WHAT YOU THINK. We may have some creative ways of getting around these limitations. When we do, we'll commit them here.
