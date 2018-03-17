#!/bin/bash
# Requires python3 and pip3
# Run with 'sudo -H'
# Baseline is in place. Can get fancy with the shell variables later to actually modify the pw set on the sql connection

apt-get update && apt-get upgrade -y
apt-get install -y python3-pip

#May need for future cloud deploy
#apt-get install -y python3-venv 

echo "Must run with sudo -H"

# Installing python flask API dependencies
pip3 install -U flask
pip3 install -U flask-cors
pip3 install -U mysql-connector

echo "Setting up DB"
echo "mysql-server-5.6 mysql-server/root_password password root" | sudo debconf-set-selections
echo "mysql-server-5.6 mysql-server/root_password_again password root" | sudo debconf-set-selections
apt-get -y install mysql-server-5.6
