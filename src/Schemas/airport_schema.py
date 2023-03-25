from main import ma
from Models.airport import Airport

# AirportSchema class inherits from ma.SQLAlchemyAutoSchema
class AirportSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Airport  # Specify the Airport model for the schema
        load_instance = True

# Initialize the AirportSchema instances
airport_schema = AirportSchema()
airports_schema = AirportSchema(many=True)