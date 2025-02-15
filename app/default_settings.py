from datetime import timedelta

SESSION_FILE_DIR="app/flask_sessions" # Custom folder for session files
SESSION_TYPE='filesystem' # Store session data in a local file
PERMANENT_SESSION_LIFETIME=timedelta(minutes=2) # Set timeout to 2 mins
