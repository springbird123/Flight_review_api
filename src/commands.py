from flask import Blueprint
from main import db
from datetime import date
import csv

from Models.user import User
from Models.review import Review
from Models.flight import Flight
from Models.airport import Airport


# Instantiate a blueprint for CLI database commands
db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Tables created")

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command('seed')


def seed_db():

    # Open the airport CSV file
    with open('./app/data/airport.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)

        # Iterate through each row in the CSV file
        for row in reader:
            # Create a new Airport object with the data from the row
            airport = Airport(airport_id=row[0], airport_name=row[1], city=row[2], country=row[3], IATA=row[4], ICAO=row[5])

            # Add the Airport object to the database session
            db.session.add(airport)

    # Commit the changes to the database
    db.session.commit()

    user1 = User(
        username = 'qantas_lover',
        email = "loveqantas@email.com",
        password = bcrypt.generate_password_hash("password123").decode("utf-8"),
    )
    db.session.add(user1)




    db.session.commit()
