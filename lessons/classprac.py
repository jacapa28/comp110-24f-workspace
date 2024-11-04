"""Working with classes."""

from __future__ import annotations
from math import sqrt


class Coordinate:

    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def get_dist(self, other: Coordinate):
        distance: float = sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
        return distance


c1: Coordinate = Coordinate(3, 1)
c2: Coordinate = Coordinate(0, 1)
print(c1.get_dist(c2))
