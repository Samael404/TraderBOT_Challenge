#!/usr/bin/python3

import mysql.connector
from datetime import date, datetime

#check for DB
def create_db():
    try:
        cmd = "CREATE DATABASE traderbot_challenge"
        cursor.execute(cmd)
    except mysql.connector.Error as err:
        print(err)
    else:
        print("OK: Created Database traderbot_challenge")

#check table
def create_tables():
    make_users = "CREATE TABLE users (username VARCHAR(30) NOT NULL UNIQUE, password VARCHAR(30) NOT NULL, created DATE NOT NULL, modified DATE NOT NULL)"
    make_trade_data = "CREATE TABLE trade_data (username VARCHAR(30) NOT NULL, trx_datetime DATETIME NOT NULL, trx_amount INT NOT NULL, acct_bal INT NOT NULL"
    m
#Will need to modify the actual fields for the trade_data & possibly the results table
    make_results = "CREATE TABLE results (username VARCHAR(30) NOT NULL UNIQUE, last_login DATETIME NOT NULL, total_tx INT NOT NULL, gain_loss INT NOT NULL)"
    
    #switch to DB
    try:
        cnx.database = "main"
    except:
        print("Failed to change to database main.")
    else:
        print("OK: Switched to database main")
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
    password = str(input("Please enter your desired password.  This cannot be changed, so make it as strong as you like: "))
    data = (username, password, date, date)
        
    try:
        cursor.execute(cmd, data)
    except mysql.connector.Error as err:
        print("Failed to insert user information into table: ", err)
    else:
        print("OK: Added user to users table.")

print("Launching DB setup...")
cnx = mysql.connector.connect(user='root', password='classpass1', host='127.0.0.1')
cursor = cnx.cursor()
create_db()
create_tables()
add_first_entry()
cnx.commit()

cursor.close()
cnx.close()
