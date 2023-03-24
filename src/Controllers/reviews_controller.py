from flask import Blueprint, request, jsonify
from main import db
from Models.review import Review
from Models.user import User
from Models.flight import Flight
from flask_jwt_extended import jwt_required, get_jwt_identity

reviews = Blueprint('reviews_controller', __name__)

# Create a review
@reviews.route('/create', methods=['POST'])
@jwt_required()
def create_review():
    # Implement review creation functionality here
    pass

# Get reviews by flight
@reviews.route('/flight/<int:flight_id>', methods=['GET'])
def get_reviews_by_flight(flight_id):
    # Implement review retrieval by flight functionality here
    pass

# Get reviews by user
@reviews.route('/user', methods=['GET'])
@jwt_required()
def get_reviews_by_user():
    # Implement review retrieval by user functionality here
    pass

# Update a review
@reviews.route('/update/<int:review_id>', methods=['PUT'])
@jwt_required()
def update_review(review_id):
    # Implement review update functionality here
    pass

# Delete a review
@reviews.route('/delete/<int:review_id>', methods=['DELETE'])
@jwt_required()
def delete_review(review_id):
    # Implement review deletion functionality here
    pass