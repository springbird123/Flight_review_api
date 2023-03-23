from flask import Blueprint, request, jsonify
from main import db, bcrypt
from Models.user import User
from Schemas.user_schema import user_schema, users_schema
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

users_controller = Blueprint('users_controller', __name__, url_prefix='/users')

# Register a user
@users_controller.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Check if user already exists
    existing_user = User.query.filter_by(username=data['username']).first()
    if existing_user:
        return jsonify({"message": "User already exists"}), 409

    # Create new user and hash the password
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], email=data['email'], password=hashed_password)

    # Save user to database
    db.session.add(new_user)
    db.session.commit()

    return jsonify(user_schema.dump(new_user)), 201

# Login a user
@users_controller.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    user = User.query.filter_by(username=data['username']).first()

    # Check if user exists and password is correct
    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.user_id)
        return jsonify({"access_token": access_token}), 200

    return jsonify({"message": "Invalid username or password"}), 401

# Update user information
@users_controller.route('/update', methods=['PUT'])
@jwt_required()
def update_user():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return jsonify({"message": "User not found"}), 404

    data = request.get_json()

    # Update user information
    if 'username' in data:
        user.username = data['username']
    if 'email' in data:
        user.email = data['email']
    if 'password' in data:
        user.password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

    db.session.commit()

    return jsonify(user_schema.dump(user)), 200

# Delete a user account
@users_controller.route('/delete', methods=['DELETE'])
@jwt_required()
def delete_user():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return jsonify({"message": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User account deleted"}), 200