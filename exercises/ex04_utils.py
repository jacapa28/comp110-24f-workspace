"""Recreating already-abstracted algorithms."""

__author__ = "730767778"


def all(ints: list[int], num: int) -> bool:
    if len(ints) == 0:
        return False
    idx = 0
    # iterates through full list
    while idx < len(ints):
        if ints[idx] != num:
            # can exit function early when element is not equal to num
            return False
        idx += 1
    return True


def max(ints: list[int]) -> int:
    # error raise
    if len(ints) == 0:
        raise ValueError("max() arg is an empty List")
    # sets the current maximum from the starting element
    max = ints[0]
    idx = 1
    # iterates through rest of the list
    while idx < len(ints):
        if ints[idx] > max:
            # sets max equal to element whenever it is bigger, making new max
            max = ints[idx]
        idx += 1
    return max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    # checks for equal length
    if len(list1) != len(list2):
        return False
    idx = 0
    # iterates through each element and compares, exits with false early if not
    while idx < len(list1):
        if list1[idx] != list2[idx]:
            return False
        idx += 1
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    idx = 0
    # iterates through all of second list and adds each element
    while idx < len(list2):
        list1.append(list2[idx])
        idx += 1
