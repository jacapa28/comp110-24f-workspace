"""Contains get_coords function for cq04"""

__author__ = "730767778"


def get_coords(xs: str, ys: str) -> None:
    i = 0
    while i < len(xs):
        j = 0
        while j < len(ys):
            print(f"({xs[i]}, {ys[j]})")
            j += 1
        i += 1
