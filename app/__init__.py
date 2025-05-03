from flask import Flask
#from flask_session import Session # for server-side sessions
from app.routes.auth import auth_bp # import blueprints
from app.routes.main import main_bp
from app.routes.tasks import tasks_bp
from flask import Flask
from app.extensions import db



# By using factory functions (like create_app()), we can create multiple app instances with different configurations, which is really helpful for testing, development, and production environments.
def create_app():
    app = Flask(__name__) # turn this file into a Flask application.

    # Configurations of app. 
    app.config.from_object('app.default_settings')

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(tasks_bp)
       
    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app