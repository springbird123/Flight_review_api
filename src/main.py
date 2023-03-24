from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# Initialize database, marshmallow, bcrypt, JWT, and CORS extensions
db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()
cors = CORS()

def create_app():
    # Initialize Flask app
    app = Flask(__name__)
    
    # Set the default configuration settings as defined in config.py
    app.config.from_object('config.app_config')
    
    # Initialize extensions with the Flask app
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)
    
    # Register CLI commands for database
    from commands import db_commands
    app.register_blueprint(db_commands)

    from Controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)
    
    
    # Define the root route for the API
    @app.route('/')
    def index():
        return {"message": "Welcome to the Flight review web server API!"}
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()