#!/usr/bin/python3
# Author: JLV, KEG
# Date: 3/2/2018
# Purpose: Connector API for web application. 
#Provides services for bot launches, data requests, and user interaction.

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

    print(" - looking for db password..." , end='')
    
    CREDS='.sql_creds'
    db_config = {
            'user': 'root',
            'password': 'classpass1',
            'host': '127.0.0.1',
            'database': 'traderbot_challenge',
                }
    output = {}

    try:
        with open(CREDS) as f:
            password = f.read()
        f.close()
        print(" OK")
    except:
        print(" FAILED. Must create password file.")
        password = getpass.getpass('Enter DB password: ')
        fo = open(CREDS, 'w')
        fo.write(password)
        print(" - created new password file: {}".format(CREDS))
    db_config['password'] = password

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
        query = ("SELECT * FROM users WHERE username = '{}'".format(user))
        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
            print("Username found.")
            output['cnx']='OK'
            output['user']=user
        else:
            print("  - Username not found in DB tables; exiting.")
            output['cnx']='OK'
            output['user']='User does not exist'
    except mysql.connector.Error as err:
        print(err)
        if err.errno == errorcode.ER_BAD_FIELD_ERROR: 
            print(err)
        elif err.errno == errorcode.ER_PARSE_ERROR:
            print("Your insert user string syntax is incorrect: ", err)
        elif err.errno == errorcode.ER_DUP_ENTRY:
            print("User entry already in Table: ", err)
    
    else:
        print("  OK - Database user segments complete.")

#The last bit of logic to add here is the update 'modified' field on new logins for existing users

    cnx.commit()    
    cursor.close()
    cnx.close()
    print("Connection closed.")    

#Still need logic here to fill in the JSON response for login, specifically add the 'modified' field.

    #output = {'user': user 'token': None}
    #return json.dumps([])
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
    return json.dumps(output)

@app.route("/scores")
def score_data():
    ''' returns db information on all bot run statistics ''' 
    output = [{'id': 0, 'user': 'test', 'bot_name': 'botA', 'bot_version': 'v1.0', 'init_total': 1000.00, 'init_final': 2000.00, 'trades_made': 5}] 
    return json.dumps(output) 

if __name__ == '__main__':
    app.run(debug=True)
