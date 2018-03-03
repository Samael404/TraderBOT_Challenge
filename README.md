
# -logo here- TraderBOT Arena

Welcome to the TraderBOT Arena project. This project is intended to be a learning exercise with the goal of creating a way to compare results of competing crypto trading bots. Currently under construction but will be updated soon.

### Architecture Diagrams
_Simple Architecture Diagram_
![Architecture Simple](/docs/architecture_simple.png)

### JSON Connectors
These are the unifying structures for data needed by the different parts of the application.

###### Results Data Structure
/scores
{
    "id": integer, unique key
    "user": string, unique key
    "bot_name": string, unique per user
    "bot_version": string, user set
    "date_started": date
    "date_ended": date
    "init_total": float
    "final_total": float
    "trades_made": integer
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
 


### Items Needed

* Python Flask API to connect web application to bot launches
* Python Flask API to connect web application to database
* Web Application to connect to make API calls to Python Flask API
* Database setup script with schema to match results expected by Web Application
  * Tables Needed: Users, Results
* Install scripts to provide dependencies and put files in correct locations.


