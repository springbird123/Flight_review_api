from flask import Blueprint
from datetime import datetime
import csv

from main import db, bcrypt
from Models.user import User
from Models.review import Review
from Models.flight import Flight
from Models.airport import Airport

# Instantiate a blueprint for CLI database commands
db_commands = Blueprint('db', __name__)

# Command to create database tables
@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Tables created")

# Command to drop database tables
@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")

# Command to seed the database with example data
@db_commands.cli.command('seed')
def seed_db():
    seed_airports()
    seed_flights()
    seed_users()
    seed_reviews()
    print("Database seeded successfully!")

# Function to seed the airports table from the CSV file
def seed_airports():
    with open("./data/airports.csv", "r", encoding="utf-8", errors='replace') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            airport = Airport(
                airport_id=row[0],
                airport_name=row[1],
                city=row[2],
                country=row[3],
                IATA=row[4],
                ICAO=row[5]
            )
            db.session.add(airport)
    db.session.commit()

# Function to seed the flights table with the specified flight
def seed_flights():
    flight1 = Flight(
        flight_id=1,
        flight_number="QF1",
        airline="Qantas",
        departure_airport_id=3361,
        arrival_airport_id=3316,
    )
    db.session.add(flight1)

    flight2 = Flight(
        flight_id=2,
        flight_number="TR13",
        airline="Scoot",
        departure_airport_id=3361,
        arrival_airport_id=3316,
    )
    db.session.add(flight2)

    db.session.commit()

# Function to seed the users table with the specified user
def seed_users():
    user = User(
        username="qantas_lover",
        email="loveqantas@email.com",
        password=bcrypt.generate_password_hash("password123").decode('utf-8'),
        admin=False
    )
    db.session.add(user)

    # Add an admin user
    admin_user = User(
        user_id = 0,
        username="admin",
        email="admin@email.com",
        password=bcrypt.generate_password_hash("admin_password").decode('utf-8'),
        admin=True
    )
    db.session.add(admin_user)

    db.session.commit()

# Function to seed the reviews table with the specified review
def seed_reviews():
    review1 = Review(
        review_id=1,
        flight_id=1,
        user_id=1,
        rating=9,
        date_flown=datetime.strptime("01Feb2023", "%d%b%Y"),
        seat_type="economy",
        aircraft_type="Airbus 320",
        description="I had a great experience on QF1. The service was excellent, and the crew was very friendly. The food was also delicious. I would definitely fly with Qantas again!"
    )
    db.session.add(review1)

    review2 = Review(
        review_id=2,
        flight_id=2,
        user_id=1,
        rating=4,
        date_flown=datetime.strptime("10Mar2023", "%d%b%Y"),
        seat_type="economy",
        aircraft_type="Boeing 787",
        description="Price was quite reasonable, but the service was not that good. Qantas is much better!"
    )
    db.session.add(review2)

    db.session.commit()
