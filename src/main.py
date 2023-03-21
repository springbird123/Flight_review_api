from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()
cors = CORS()

def create_app():
    
    app = Flask(__name__)
    # cors = CORS(app, resources={r"/*": {"origins": "*"}})
    cors.init_app(app, resources={r"/*": {"origins": "*", "methods": "*"}})
    
    # Set the default configuration settings as defined in config.py
    app.config.from_object('config.app_config')
    
    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    
    # Register CLI commands for database
    from commands import db_commands
    app.register_blueprint(db_commands)

    
    
    @app.route('/')
    def index():
        {"message": "Welcome to the Flight review web server API!"}
    
    return app