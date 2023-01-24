

import requests
from datetime import datetime,timedelta





import psycopg2
from flask import Flask, request, jsonify

app = Flask(__name__)

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="pg_Admin",
    database="Database_1",
    user="Postuser",
    password="postuser"
)

# Create a cursor to interact with the database
cursor = conn.cursor()

# Handle user creation
@app.route("/create_user", methods=["POST"])

def create_user():
    # Retrieve the user's information from the request
    user_data = request.get_json()
    username = user_data["username"]
    password = user_data["password"]
    email = user_data["email"]

    # Insert the user's information into the database
    cursor.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)", (username, password, email))
    conn.commit()

    # Return a message indicating that the user was successfully created
    return jsonify({"message": "User created successfully"})

# Handle user login
@app.route("/login", methods=["POST"])

def login():
    # Retrieve the user's login information from the request
    login_data = request.get_json()
    username = login_data["username"]
    password = login_data["password"]

    # Retrieve the user's information from the database
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()

    if user is not None:
        # Update the last_login field in the user's record
        cursor.execute("UPDATE users SET last_login = NOW() WHERE username = %s", (username,))
        conn.commit()

        # Return a message indicating that the login was successful
        return jsonify({"message": "Login successful"})
    else:
        # Return a message indicating that the login was unsuccessful
        return jsonify({"message": "Invalid username or password"})

# Run the app
if __name__ == "__main__":
    app.run(debug=True)


































