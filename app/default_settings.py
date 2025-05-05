from datetime import timedelta
import json

try:
    with open('secrets.json', 'r') as file:
        secrets = json.load(file) # returns a dictionary
except FileNotFoundError:
    secrets={"SESSION_SECRET_KEY": "007"}

SESSION_FILE_DIR="app/flask_sessions" # Custom folder for session files
SESSION_TYPE='filesystem' # Store session data in a local file
PERMANENT_SESSION_LIFETIME=timedelta(minutes=2) # Set timeout to 2 mins
# There is also a second object called session which allows you to store information specific to a user from one request to the next. 
# In order to use sessions you have to set a secret key.
SECRET_KEY=secrets["SESSION_SECRET_KEY"] 
SQLALCHEMY_DATABASE_URI="sqlite:///users.db" # uses by default the "instance" folder.
