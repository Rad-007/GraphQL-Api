

import requests
from pymongo import MongoClient


from datetime import datetime, timedelta
from flask import Flask, request
import os



app = Flask(__name__)

@app.route('/like_share_comment', methods=['GET'])

def like_share_comment(user_id,access_token):

# Replace ACCESS_TOKEN with a valid access token
    

    # Replace USER_ID with the ID of the user
    user_id = os.environ('user_id')

    # Make a GET request to the Graph API
    url = f'https://graph.facebook.com/v10.0/{user_id}?fields=id,name,likes,shares,comments&access_token={access_token}'
    response = requests.get(url)

    # Get the JSON data from the response
    data = response.json()

    # Get the total likes, shares, and comments
    total_likes = data['likes']
    total_shares = data['shares']
    total_comments = data['comments']

    client=MongoClient()

    db2 = client.like_database

        # Create a new collection (table)
    users = db2.likes
    users.insert_one(data)


    return (data)




if __name__ == '__main__':
    app.run(debug=True)