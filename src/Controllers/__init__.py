from .users_controller import users
from .flights_controller import flights
from .reviews_controller import reviews
from .auth_controller import auth

registerable_controllers = [
    auth,
    users,
    flights,
    reviews
]