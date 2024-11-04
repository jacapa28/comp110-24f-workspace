"""Summing the elements of a list using different loops"""

__author__ = "730767778"


def w_sum(vals: list[float]) -> float:
    sum: float = 0.0
    idx: int = 0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for num in vals:
        sum += num
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for i in range(0, len(vals)):
        sum += vals[i]
    return sum
