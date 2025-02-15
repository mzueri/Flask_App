import os
from datetime import timedelta

SESSION_FILE_DIR="app/flask_sessions" # Custom folder for session files
SESSION_TYPE='filesystem' # Store session data in a local file
PERMANENT_SESSION_LIFETIME=timedelta(minutes=2) # Set timeout to 2 mins
SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'default_fallback_key') # Secret key for session encryption taken from environment variable (for security reasons, the key should never be committed). If no secret key is provided, then use 'top_secret_key_007' (default, not secure either).

