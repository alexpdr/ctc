"""App module"""
from typing import List

from .greetings import router as greetings_router

ROUTERS: List = [
    greetings_router
]
