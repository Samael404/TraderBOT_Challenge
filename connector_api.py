#!/usr/bin/python3
# Author: JLV, KEG
# Date: 3/2/2018
# Purpose: Connector API for web application. 
#    Provides services for bot launches, data requests, and user interaction.

from flask import Flask
from flask_cors import CORS, cross_origin
import json
import os
from shutil import copy2
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime

app = Flask(__name__)
CORS(app)


@app.route("/login/<user>")
def login(user):
    ''' provide simple (read - insecure) authentication '''
    print("User Submitted: {}".format(user))

    db_config = {
            'user': 'root',
            'password': 'classpass1',
            'host': '127.0.0.1',
            'database': 'traderbot_challenge',
                }

    #Checks the DB connection
    try:
        cnx = mysql.connector.connect(**db_config)
        print("Connection succeeded.") 
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    #Tries to query the username and checks if it's in the user table or not
    cursor = cnx.cursor(buffered=True)

    try:
        query = ("SELECT * FROM users WHERE username = '%s'")
        query_data = str(user)
        cursor.execute(query, query_data)
#I tried adding the below if statement in, but with it here it does not print the 'username found' yet still moves to the else block below
#Without the 'if', it prints 'username found' even if it's not in the table
      # if cursor.rowcount==1:
        print("Username found.")
    
    except mysql.connector.Error as err:
        print(err)
        if err.errno == errorcode.ER_BAD_FIELD_ERROR: 
            cmd = ("INSERT INTO users (username, password, created, modified)"            "VALUES (%s, %s, %s, %s)") 
            date = datetime.now().date()
            cmd_values = (str(user), 'password', str(date), str(date))
            cursor.execute(cmd, cmd_values)
            if err.errno == errorcode.ER_PARSE_ERROR:
                print("Your insert user string syntax is incorrect.")
        elif err.errno == errorcode.ER_DUP_ENTRY:
            print("User entry already in Table.")
    
    else:
        print("OK")

    cnx.commit()    
    cursor.close()
    cnx.close()
    print("Connection closed.")    

#Still need logic here to fill in the JSON response for login.

    output = {'user': user, 'token': None}
    return json.dumps(output)


@app.route("/bots/<user>")
def bot_info(user):
    ''' provide information on user bots '''
    path = os.path.expanduser("~/TraderBOT_Challenge/bots")
    path = os.chdir(path)
    path = os.getcwd()
    active_user = str(path) + '/' + str(user)
    
    if os.path.isdir(active_user):
        print("{} username is selected.  Changing to user directory.".format(user))
        os.chdir(active_user)
    else:
        os.mkdir(active_user)
        print("Created {} user directory. Adding default bot to directory and changing to use new user directory.".format(user))
        new_user = os.chdir(active_user)
        copy2(path + '/' + 'bot.py', active_user)

    bots_available = []

    for root, dirs, files in os.walk('.', topdown=False):
        for item in files:
            bots_available += files
    
    output = {'user': user, 'bots_available': bots_available}
    return json.dumps(output) 

@app.route("/bots/<user>/<bot_name>/start")
def bot_launch(user, bot_name):
    ''' launch a bot '''
    path = os.path.expanduser("~/TraderBOT_Challenge/bots/" + str(user))
    path = os.chdir(path)
        
    output = {'user': user, 'bot_name': bot_name, 'launch': True}
    # TODO: Suggestion to utilize importlib functionality to dynamically try and load path of python bot
    # - then your requirement will be to have the same hook in calls for every bot (aka a template file will be needed)
    # - function will return failure if the bot hasn't been found - otherwise always a success
    # - will have to launch a async thread for bot and check back on a regular basis for results
    # - which means this function will be responsible for writing to the database
    # - suggestion to manage extra threads by storing bot_name, user, and pid in this api - that way if we could check if a process is still running
    # - simpler method would be to just have another api call for the bots to make but that is sloppier long term
    return json.dumps(output)

@app.route("/scores")
def score_data():
    ''' returns db information on all bot run statistics ''' 
    output = [{'id': 0, 'user': 'test', 'bot_name': 'botA', 'bot_version': 'v1.0', 'init_total': 1000.00, 'init_final': 2000.00, 'trades_made': 5}] 
    # TODO: Must query db for real data
    return json.dumps(output) 

if __name__ == '__main__':
    app.run(debug=True)
