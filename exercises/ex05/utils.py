"""Functions with lists."""

__author__ = "730767778"


def only_evens(ints: list[int]) -> list[int]:
    """Adds even numbers to new list and returns list"""
    # initializes empty list
    new = []
    # iterates over full list checking for evens and adding them to new
    for i in ints:
        if i % 2 == 0:
            new.append(i)
    return new


def sub(ints: list[int], start: int, end: int) -> list[int]:
    """Adds ints from certain subsection of list to new list and returns it"""
    if len(ints) == 0 or start >= len(ints) or end <= 0:
        return []
    # initalizes important variables
    idx = 0
    new = []
    # if start is less than 0, it will start at zero. if higher, it starts at start
    if start > 0:
        idx = start
    # if end is any bigger than list, end becomes the final index of list
    if end >= len(ints):
        end = len(ints)
    # iterates through list at specified indexes and adds to new
    while idx < end:
        new.append(ints[idx])
        idx += 1
    return new


def add_at_index(ints: list[int], num: int, idx: int) -> None:
    """Adds number at specified index in list"""
    if idx < 0 or idx > len(ints):
        raise IndexError("Index is out of bounds for the input list")
    # adds empty spot at end of list
    ints.append(0)
    i = len(ints) - 1
    # iterates through list backwards, shifting each element before it to the right
    while i > idx:
        ints[i] = ints[i - 1]
        i -= 1
    # changes list at index to specified number now that everything has been moved
    ints[idx] = num
