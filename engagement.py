


import requests
from  datetime import datetime,timedelta

from pymongo import MongoClient

import os

# Replace YOUR_ACCESS_TOKEN with a valid access token


from datetime import datetime, timedelta
from flask import Flask, request

app = Flask(__name__)

@app.route('/engagement', methods=['GET'])


def engagement(user_id,access_token):

# Replace USER_ID with the ID of the user you want to retrieve information about
    

    
    
    
    

    # Start and end date of the date range (in YYYY-MM-DD format)
    start_date = 'YYYY-MM-DD'
    end_date = 'YYYY-MM-DD'

    # URL to make the API request
    url = f'https://graph.facebook.com/v8.0/{user_id}/engagements?access_token={access_token}&since={start_date}&until={end_date}'

    # Make the API request
    response = requests.get(url)

    # Get the JSON data from the response
    data = response.json()

    # Create an empty dictionary to store the latest engagement of the day
    latest_engagements = {}

    # Iterate through the engagement data
    for engagement in data['data']:
        # Get the engagement date
        engagement_date = datetime.datetime.strptime(engagement['created_time'], '%Y-%m-%dT%H:%M:%S+0000')
        engagement_date = engagement_date.date()
        # Check if an engagement for the same date already exists in the dictionary
        if engagement_date in latest_engagements:
            # Compare the engagement time with the existing engagement
            existing_engagement_time = datetime.datetime.strptime(latest_engagements[engagement_date]['created_time'], '%Y-%m-%dT%H:%M:%S+0000')
            current_engagement_time = datetime.datetime.strptime(engagement['created_time'], '%Y-%m-%dT%H:%M:%S+0000')
            if current_engagement_time > existing_engagement_time:
                # If the current engagement is later, update the dictionary
                latest_engagements[engagement_date] = engagement
        else:
            # If no engagement for the same date exists, add the engagement to the dictionary
            latest_engagements[engagement_date] = engagement

    # Print the latest engagements
    


    client=MongoClient()

    db2 = client.engage_database

    # Create a new collection (table)
    users = db2.engagements
    users.insert_one(latest_engagements)
    
    return(latest_engagements)







if __name__ == '__main__':
    app.run(debug=True)







