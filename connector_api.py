#!/usr/bin/python3
# Author: JLV
# Date: 3/2/2018
# Purpose: Connector API for web application. 
#    Provides services for bot launches, data requests, and user interaction.

from flask import Flask
from flask_cors import CORS, cross_origin
import json
import os
from shutil import copy2

app = Flask(__name__)
CORS(app)

@app.route("/login/<user>")
def login(user):
    ''' provide simple (read - insecure) authentication '''
    print("User Submitted: {}".format(user))
###  Need to update the logic here to connect to DB and login information.  The script needs to check if a user exists in the DB, create if not, and return the user information.  We are ignoring tokenization for now.      
#    try:
#       check db for user
#    except:
#       print user does not exist, creating new user
    output = {'user': user, 'token': None}
    return json.dumps(output)

@app.route("/bots/<user>")
def bot_info(user):
    ''' provide information on user bots '''
    path = "/home/kgarre/TraderBOT_Challenge/bots"
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
    path = "/home/kgarre/TraderBOT_Challenge/bots/" + str(user)
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
