
from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session # for server-side sessions
from datetime import timedelta

# By using factory functions (like create_app()), we can create multiple app instances with different configurations, which is really helpful for testing, development, and production environments.
def create_app():
    app = Flask(__name__) # turn this file into a Flask application.


    app.secret_key = 'top_secret_key_007' # Secret key for session encryption
    app.config['SESSION_TYPE'] = 'filesystem' # Store session data in a local file
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=2) # Set timeout to 2 mins
    app.config['SESSION_FILE_DIR'] = './flask_sessions'  # Custom folder for session files
    Session(app) # Initialize session on server-side

    # Import and register blueprints
    from app.routes.auth import auth_bp
    from app.routes.main import main_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    return app