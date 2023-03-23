from .users_controller import users_controller
from .flights_controller import flights_controller
from .reviews_controller import reviews_controller

registerable_controllers = [
    users_controller,
    flights_controller,
    reviews_controller
]