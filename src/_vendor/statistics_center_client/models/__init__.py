"""Contains all the data models used in inputs/outputs"""

from .games import Games
from .login import Login
from .login_success import LoginSuccess
from .statistics import Statistics

__all__ = (
    "Games",
    "Login",
    "LoginSuccess",
    "Statistics",
)
