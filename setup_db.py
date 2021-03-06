#!/usr/bin/python3

import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime
import getpass

#Remove the password from the file before pushing to master
dbcreds = { 'user': 'root', 'password': '', 'database': '', 'host': '127.0.0.1' }
CREDS='.sql_creds'

#This connection test will fail the first time, depending on how the mysql DB password was first set
def get_creds():
    print(" - testing connection to db...", end='')
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
    dbcreds['password'] = password.rstrip()

#check for DB
def db_connect():

    try:
        cnx = mysql.connector.connect(**dbcreds)
        print(" OK - Connected to DB.")
        return cnx
    except mysql.connect.Error as err:
        print(" FAILED with the following error: ", err)
        return False

def create_db():
    try:
        cmd = "CREATE DATABASE traderbot_challenge"
        cursor.execute(cmd)
        dbcreds['database'] = "traderbot_challenge"
    except mysql.connector.Error as err:
        print("Error creating traderbot_challenge database: ", err)
    else:
        print("OK: Created Database traderbot_challenge")


#check table
def create_tables():
    make_users = "CREATE TABLE users (username VARCHAR(30) NOT NULL UNIQUE, password VARCHAR(30) NOT NULL, created DATE NOT NULL, modified DATE NOT NULL)"
    make_trade_data = "CREATE TABLE trade_data (username VARCHAR(30) NOT NULL, bot_name VARCHAR(30) NOT NULL, bot_ver INT(3), trx_datetime DATETIME NOT NULL, total_trx INT NOT NULL, avg_gain INT NOT NULL, start_bal INT NOT NULL, end_bal INT NOT NULL, tot_acct_bal INT NOT NULL, runtime INT NOT NULL)"
    
#Will need to modify the actual fields for the trade_data & possibly the results table
    make_results = "CREATE TABLE results (username VARCHAR(30) NOT NULL UNIQUE, bot_name VARCHAR(30) NOT NULL, bot_ver VARCHAR(5) NOT NULL, last_login DATETIME NOT NULL, total_tx INT NOT NULL, gain_loss INT NOT NULL)"
    
    #switch to DB
    try:
        cnx.database = "traderbot_challenge"
    except:
        print("Failed to change to database traderbot_challenge.")
    else:
        print("OK: Switched to database traderbot_challenge")
    #actually create tables
    try:
        cursor.execute(make_users)
    except mysql.connector.Error as err:
        print("Failed to create users table: ", err)
    else:
        print("OK: Created the 'users' table")

    try:
        cursor.execute(make_trade_data)
    except mysql.connector.Error as err:
        print("Failed to create trade_data table: ", err)
    else:
        print("OK: Created the 'trade_data' table")

    try:
        cursor.execute(make_results)
    except mysql.connector.Error as err:
        print("Failed to create results table: ", err)
    else:
        print("OK: Created the 'results' table")

def add_first_entry():
    cmd = "INSERT INTO users (username, password, created, modified) VALUES (%s, %s, %s, %s)"
    date = str(datetime.now().date())
    username = str(input("Please enter your desired username: "))
    password = str(input("Please enter your desired user password.  This cannot be changed, so make it as strong as you like: "))
    data = (username, password, date, date)
        
    try:
        cursor.execute(cmd, data)
    except mysql.connector.Error as err:
        print("Failed to insert user information into table: ", err)
    else:
        print("OK: Added user to users table.")


if __name__ == '__main__':
    print("Launching mySQL setup...")
    get_creds()
    cnx = db_connect()
    if cnx == False:
        exit(1)
    cursor = cnx.cursor()
    create_db()
    create_tables()
    add_first_entry()
    cnx.commit()
    cursor.close()
    cnx.close()
    exit(0)
