__author__ = "730767778"


def find_and_remove_max(ints: list[int]) -> int:
    if len(ints) == 0:
        return -1
    max = ints[0]
    for i in ints:
        if i > max:
            max = i
    idx = 0
    while idx < len(ints):
        if ints[idx] == max:
            ints.pop(idx)
        else:
            idx += 1
    return max
