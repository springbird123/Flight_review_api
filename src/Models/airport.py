from main import db


class Airport(db.Model):
    __tablename__ = "airports"
    
    airport_id = db.Column(db.Integer, primary_key=True)
    #different flights can have the same flight number. For example, QF1 represents SYD-SIN and SIN-LHY two routes.
    airport_name = db.Column(db.String(), nullable=False)
    city = db.Column(db.String(), nullable=False)
    country = db.Column(db.String(), nullable=False)
    IATA = db.Column(db.String()) #three-character alphanumeric geocode designating airports around the world by the International Air Transport Association
    ICAO = db.Column(db.String(), nullable=False)
    #flights_departure = db.relationship("Flight", foreign_keys=[Flight.departure_airport_id], cascade="all, delete")
    #flights_arrival = db.relationship("Flight", foreign_keys=[Flight.arrival_airport_id], cascade="all, delete")