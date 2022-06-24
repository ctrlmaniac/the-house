"""This file is responsible of exporting all rooms."""
from .bedroom import Bedroom
from .hall import Hall
from .hallway import Hallway
from .studio import Studio


__all__ = [
    "Bedroom",
    "Hall",
    "Hallway",
    "Studio",
]
