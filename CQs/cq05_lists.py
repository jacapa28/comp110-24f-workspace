"""Mutating functions."""

__author__ = "730767778"


def manual_append(ints: list[int], num: int) -> None:
    ints.append(num)


def double(ints: list[int]) -> None:
    idx = 0
    while idx < len(ints):
        ints[idx] = ints[idx] * 2
        idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
