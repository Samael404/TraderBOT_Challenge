
# -logo here- TraderBOT Arena

Welcome to the TraderBOT Arena project. This project is intended to be a learning exercise with the goal of creating a way to compare results of competing crypto trading bots. Currently under construction but will be updated soon.

### Installation Files and Instructions
install.sh
--> Installs package dependencies for Python, downloads and performs basic mySQL database configuration
--> sh install.sh

setup_db.py
--> Runs through the database creation and table setup with default user
--> python3 setup_db.py
### Architecture Diagrams
_Simple Architecture Diagram_
![Architecture Simple](/docs/architecture_simple.png)

### JSON Connectors
These are the unifying structures for data needed by the different parts of the application.

###### Results Data Structure Output from Bot activity
/scores
{
    "username": varchar(30), unique key
    "bot_name":varchar(30)
    "bot_ver": int(3)
    "last_login": datetime
    "total_tx": int(11) 
    "gain_loss": int(11)
}

###### Users Data Structure
api location: /login/\<user\>
info: get simple login information
{
    "user": string, unique key
    "token": to be implemented
    "last_login": date
}
###### Python Bot Launch Data Structure
api location: /bot/\<user\>
info: get available bots for user
{
    "user": string
    "bots_available": [ "name1", "name2" ... ]
}
api location: /bot/\<user\>/\<bot_name\>\start
info: launch specific user bot
{
    "user": string 
    "bot_name": string
    "parameters": [
                      {"name":"value"},
		      ...
                  ] 
}

