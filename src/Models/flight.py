from main import db


class Flight(db.Model):
    __tablename__ = "flights"
    
    flight_id = db.Column(db.Integer, primary_key=True)
    #different flights can have the same flight number. For example, QF1 represents SYD-SIN and SIN-LHY two routes.

    flight_number = db.Column(db.String(), nullable=False)
    departure_airport_id = db.Column(db.Integer,db.ForeignKey('airports.airport_id'))
    arrival_airport_id = db.Column(db.Integer,db.ForeignKey('airports.airport_id'))
    reviews = db.relationship("Review", back_populates="flight", cascade="all, delete")
    departure_airport = db.relationship("Airport", foreign_keys=[departure_airport_id])
    arrival_airport = db.relationship("Airport", foreign_keys=[arrival_airport_id])


