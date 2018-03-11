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
    return json.dumps(output)

@app.route("/scores")
def score_data():
    ''' returns db information on all bot run statistics ''' 
    output = [{'id': 0, 'user': 'test', 'bot_name': 'botA', 'bot_version': 'v1.0', 'init_total': 1000.00, 'init_final': 2000.00, 'trades_made': 5}] 
    return json.dumps(output) 

if __name__ == '__main__':
    app.run(debug=True)