"""Working with classes"""

__author__ = "730767778"

from __future__ import annotations


class Point:
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        new_point: Point = Point(x_init=self.x * factor, y_init=self.y * factor)
        return new_point
