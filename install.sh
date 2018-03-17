#!/bin/bash
# Requires python3 and pip3
# Run with 'sudo -H'

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
echo Please enter a password for your local database:

read varname 

echo $varname > .sql_creds
#Not sure about the following 2 echo lines
echo "mysql-server mysql-server/root_password password $varname" | sudo debconf-set-selections
echo "mysql-server mysql-server/root_password_again password $varname" | sudo debconf-set-selections
apt-get -y install mysql-server

echo -e "$varname\nn\nY\nY\nY\nY\n" | mysql_secure_installation
