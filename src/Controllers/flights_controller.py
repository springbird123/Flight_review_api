from flask import Blueprint, request, jsonify
from Models.flight import Flight
from Models.airport import Airport
from Schemas.flight_schema import flight_schema, flights_schema
from main import db
from flask_jwt_extended import jwt_required, get_jwt_identity

flights = Blueprint('flights_controller', __name__, url_prefix='/flights')

# Get a flight by ID
@flights.route('/id/<int:flight_id>', methods=['GET'])
def get_flight_by_id(flight_id):
    flight = Flight.query.get(flight_id)

    if not flight:
        return jsonify({"message": "Flight not found"}), 404

    return jsonify(flight_schema.dump(flight))

# Get flights by departure and arrival airport's city or IATA, or by flight number
@flights.route('/search', methods=['GET'])
def get_flights_by_airports_or_flight_number():
    departure = request.args.get('departure', None)
    arrival = request.args.get('arrival', None)
    flight_number = request.args.get('flight_number', None)

    query = Flight.query.join(Flight.departure_airport).join(Flight.arrival_airport)

    if departure and arrival:
        query = query.filter(
            (Airport.city == departure) | (Airport.iata == departure),
            (Flight.arrival_airport.has((Airport.city == arrival) | (Airport.iata == arrival)))
        )
    elif flight_number:
        query = query.filter(Flight.flight_number == flight_number)

    flights = query.all()

    if not flights:
        return jsonify({"message": "No flights found"}), 404

    return jsonify(flights_schema.dump(flights))

# Add a flight
@flights.route('/add', methods=['POST'])
def add_flight():
    flight_number = request.json['flight_number']
    airline = request.json['airline']
    departure_airport_id = request.json['departure_airport_id']
    arrival_airport_id = request.json['arrival_airport_id']

    new_flight = Flight(flight_number=flight_number, airline=airline, departure_airport_id=departure_airport_id, arrival_airport_id=arrival_airport_id)
    db.session.add(new_flight)
    db.session.commit()