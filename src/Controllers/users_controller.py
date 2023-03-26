from flask import Blueprint, jsonify, request, abort
from main import db, bcrypt
from Models.user import User
from Schemas.user_schema import user_schema, users_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from .auth_controller import admin_required

users = Blueprint('users_controller', __name__, url_prefix='/users')


# Getting the list of all users (admin required)
@users.route("/", methods=["GET"])
@jwt_required()
@admin_required
def get_all_users():
    users = User.query.all()
    return jsonify(users_schema.dump(users))

# Getting a specific user by ID (admin required)
@users.route("/<int:user_id>", methods=["GET"])
@jwt_required()
@admin_required
def get_user(user_id):
    # Find the user in the db based on their ID
    user = User.query.get_or_404(user_id)
    return jsonify(user_schema.dump(user))

# Updating a user's details
@users.route("/<int:id>/", methods=["PUT"])
@jwt_required()
def update_user(id):
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()

    if user.id != id:
        return abort(401, description="You are not authorized to update this user")

    user_fields = user_schema.load(request.json)
    # Try to extract the required fields and catch KeyError if any field is missing
    try:
        user_name = user_fields["user_name"]
        email = user_fields["email"]
        password = user_fields["password"]
    except KeyError:
        return abort(400, description="Missing data for required fields")
        
    # Create a new User object, and set its attributes
    user.user_name = user_name
    user.email = email
    user.password = bcrypt.generate_password_hash(password).decode("utf-8")
    user.admin = False

    db.session.commit()

    return jsonify(user_schema.dump(user))


# Grant admin privileges to a user((admin required))
@users.route("/<int:user_id>/admin", methods=["PUT"])
@jwt_required()
@admin_required
def set_admin(id):
    user = User.query.get_or_404(id)
    # Update the 'admin' field of the user to True
    user.admin = True
    db.session.commit()

    # Return a success message along with the updated user data
    return jsonify({"message": "Admin privileges granted to the user", "user": user_schema.dump(user)})


# Delete the user 
@users.route("/<int:id>/", methods=["DELETE"])
@jwt_required()
def delete_user(id):
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()
    
    # Check if the user_id associated with the review matches the user_id from the JWT token, or if the user is an admin
    if user.id != id and not user.admin:
        return abort(401, description="You are not authorized to delete this user")

    db.session.delete(user)
    db.session.commit()

    return jsonify(user_schema.dump(user))

