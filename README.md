
# -logo here- TraderBOT Arena

Welcome to the TraderBOT Arena project. This project is intended to be a learning exercise with the goal of creating a way to compare results of competing crypto trading bots. Currently under construction but will be updated soon.

### Architecture Diagrams

![Architecture Simple](/docs/architecture_simple.png)

### JSON Connectors
These are the unifying structures for data needed by the different parts of the application.

###### Results Data Structure
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
{
    "user": string, unique key
    "token": to be implemented
    "bots_available": [ "name1", "name2", ... ]
}

###### Python Bot Launch Data Structure
{
    "user": string 
    "bot_name": string
    "bot_version": string
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


