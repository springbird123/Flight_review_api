from flask import Blueprint, request, jsonify,abort
from main import db
from Models.review import Review
from Models.user import User
from Models.flight import Flight
from Schemas.review_schema import review_schema, reviews_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError

reviews = Blueprint('reviews_controller', __name__, url_prefix='/reviews')

# Get reviews by flight ID
@reviews.route('/flight/<int:flight_id>', methods=['GET'])
def get_reviews_by_flight(flight_id):
    flight = Flight.query.get_or_404(flight_id)
    reviews = Review.query.filter_by(flight_id=flight_id).all()
    return jsonify(reviews_schema.dump(reviews))

# Get reviews by user ID
@reviews.route('/user/<int:user_id>', methods=['GET'])
@jwt_required()
def get_reviews_by_user(user_id):
    user = User.query.get_or_404(user_id)
    reviews = Review.query.filter_by(user_id=user_id).all()
    return jsonify(reviews_schema.dump(reviews))

# Add a review
@reviews.route('/', methods=['POST'])
@jwt_required()
def add_review():
    data = request.get_json()

    current_user_id = get_jwt_identity()

    # Check if flight exists
    flight = Flight.query.get(data['flight_id'])
    if not flight:
        return jsonify({"message": "Flight not found"}), 404

    new_review = Review(
        flight_id=data['flight_id'],
        user_id=current_user_id,
        rating=data['rating'],
        date_flown=data['date_flown'],
        seat_type=data['seat_type'],
        aircraft_type=data['aircraft_type'],
        description=data['description']
    )

    db.session.add(new_review)
    db.session.commit()

    return jsonify(review_schema.dump(new_review)), 201

# Update a review
@reviews.route('/<int:review_id>', methods=['PUT'])
@jwt_required()
def update_review(review_id):
    # Get the user_id from the JWT token
    user_id = get_jwt_identity()
    
    # Get the review by ID
    review = Review.query.get_or_404(review_id)
    
    # Check if the user_id associated with the review matches the user_id from the JWT token
    if review.user_id != user_id:
        return abort(401, description="You are not authorized to update this review")
    
    data = request.get_json()

    review.rating = data['rating']
    review.date_flown = data['date_flown']
    review.seat_type = data['seat_type']
    review.aircraft_type = data['aircraft_type']
    review.description = data['description']

    db.session.commit()

    return jsonify(review_schema.dump(review))


# Delete a review
@reviews.route('/<int:review_id>', methods=['DELETE'])
@jwt_required()
def delete_review(review_id):
    # Get the user_id from the JWT token
    user_id = get_jwt_identity()
    
    # Get the user from the database
    user = User.query.get(user_id)

    # Get the review by ID
    review = Review.query.get_or_404(review_id)
    
    # Check if the user_id associated with the review matches the user_id from the JWT token, or if the user is an admin
    if review.user_id != user_id and not user.admin:
        return abort(401, description="You are not authorized to delete this review")

    db.session.delete(review)
    db.session.commit()

    return jsonify({"message": "Review successfully deleted"})