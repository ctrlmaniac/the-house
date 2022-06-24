"""This file is responsible of exporting all rooms."""
from .bedroom import Bedroom
from .hall import Hall
from .hallway import Hallway
from .kitchen import Kitchen
from .studio import Studio


__all__ = [
    "Bedroom",
    "Hall",
    "Hallway",
    "Kitchen",
    "Studio",
]
