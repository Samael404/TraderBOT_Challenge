#!/usr/bin/python3
# Author: JLV
# Date: 3/2/2018
# Purpose: Connector API for web application. 
#    Provides services for bot launches, data requests, and user interaction.

from flask import Flask
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app)

@app.route("/login/<user>")
def login(user):
    ''' provide simple (read - insecure) authentication '''
    print("User Submitted: {}".format(user))
    output = {'user': user, 'token': None}
    return json.dumps(output)

@app.route("/bot/<user>")
def bot_info(user):
    ''' provide information on user bots '''
    output = {'user': user, 'bots_available': ["botA", "botB"]}
    return json.dumps(output) 

@app.route("/bot/<user>/<bot_name>/start")
def bot_launch(user, bot_name):
    ''' launch a bot '''
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