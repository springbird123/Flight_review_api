from main import db


class Review(db.Model):
    __tablename__ = 'reviews'

    review_id = db.Column(db.Integer, primary_key=True)
    flight_id = db.Column(db.Integer, db.ForeignKey("flights.flight_id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    date_flown = db.Column(db.Date, nullable=False)
    seat_type = db.Column(db.String, nullable=False)
    aircraft_type = db.Column(db.String)
    description = db.Column(db.String)
    user = db.relationship("User", back_populates="reviews")
    flight = db.relationship("Flight", back_populates="reviews", cascade="all, delete")
