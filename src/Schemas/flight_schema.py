from main import ma
from Models.flight import Flight
from Schemas.airport_schema import AirportSchema

# FlightSchema class inherits from ma.SQLAlchemyAutoSchema
class FlightSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Flight  # Specify the Flight model for the schema
        load_instance = True

    # Use nested AirportSchema to include departure and arrival airport details
    departure_airport = ma.Nested(AirportSchema())
    arrival_airport = ma.Nested(AirportSchema())

# Initialize the FlightSchema instances
flight_schema = FlightSchema()
flights_schema = FlightSchema(many=True)