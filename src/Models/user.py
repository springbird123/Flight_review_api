from main import db


class User(db.Model):
    __tablename__ = "users"
    
    # Defining columns for the User table
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    admin = db.Column(db.Boolean(), nullable=False)
    # Define the relationship between User and Review
    reviews = db.relationship("Review", back_populates="user", cascade="all, delete") # One-to-many relationship with Review

