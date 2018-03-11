#!/usr/bin/python3
# Author: JLV
# Date: 3/11/2018
# Purpose: Setup Database for application

import mysql.connector
from mysql.connector import errorcode
import getpass
from datetime import date, datetime

CREDS='.sql_creds'
dbcreds = { 'user': 'root', 'password': '', 'host': '127.0.0.1' }
conn = ''

def get_db_password():
    print(" - looking for db password..." , end='')
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
    dbcreds['password'] = password

def connect_db():
    print(" - testing connection to db...", end='')
    try:
        cnx = mysql.connector.connect(**dbcreds)
        print(" OK")
    except:
        print(" FAILED")


if __name__ == '__main__':
    print("Setting up mySQL...")
    get_db_password()
    connect_db()
    exit(0)
