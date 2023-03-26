from flask import Blueprint, request, jsonify, abort
from main import db, bcrypt
from Models.user import User
from Schemas.user_schema import user_schema
from datetime import timedelta
from flask_jwt_extended import create_access_token, get_jwt_identity
from functools import wraps

auth = Blueprint('auth_controller', __name__, url_prefix='/auth')

@auth.route('/register', methods=['POST'])
def auth_register():
    # Load the request data
    user_fields = user_schema.load(request.json)

    # Check if the email is already registered
    user = User.query.filter_by(email=user_fields["email"]).first()
    if user:
        return abort(400, description="Email already registered")

    # Create a new user with the request data and hashed password
    new_user = User(
        username=user_fields["user_name"],
        email=user_fields["email"],
        password=bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8")
    )

    # Add the new user to the database and commit the changes
    db.session.add(new_user)
    db.session.commit()

    # Create an access token with a 1-day expiry
    expiry = timedelta(days=1)
    access_token = create_access_token(identity=str(new_user.id), expires_delta=expiry)

    # Return the user email and the access token
    return jsonify({"user": new_user.email, "token": access_token})

@auth.route('/login', methods=['POST'])
def auth_login():
    # Load the request data
    user_fields = user_schema.load(request.json)

    # Check if the user exists in the database
    user = User.query.filter_by(email=user_fields["email"]).first()

    # Verify the password and create an access token if it's correct
    if user and bcrypt.check_password_hash(user.password, user_fields["password"]):
        expiry = timedelta(days=1)
        access_token = create_access_token(identity=str(user.id), expires_delta=expiry)
        return jsonify({"user": user.email, "token": access_token})
    else:
        return abort(401, description="Incorrect username and password")

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        user_id = get_jwt_identity()
        user = User.query.get(user_id)

        # Check if the user is an admin and abort if not
        if not user.admin:
            abort(401, description="Unauthorized user")

        return fn(*args, **kwargs)

    return wrapper