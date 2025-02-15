from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session # for server-side sessions

# By using factory functions (like create_app()), we can create multiple app instances with different configurations, which is really helpful for testing, development, and production environments.
def create_app():
    app = Flask(__name__) # turn this file into a Flask application.

    # Configurations of app. 
    app.config.from_object('app.default_settings')

    Session(app) # Initialize session on server-side

    # Import and register blueprints
    from app.routes.auth import auth_bp
    from app.routes.main import main_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    return app