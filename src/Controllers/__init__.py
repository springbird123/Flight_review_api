from .users_controller import users
from .flights_controller import flights
from .reviews_controller import reviews

registerable_controllers = [
    users,
    flights,
    reviews
]