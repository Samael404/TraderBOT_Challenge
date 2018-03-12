#!/bin/bash
# Requires python3 and pip3

echo "Must run with sudo -H"

# Installing python flask API dependencies
pip3 install -U flask
pip3 install -U flask-cors
pip3 install -U mysql-connector

echo "Setting up DB"
apt-get install mysql-server
