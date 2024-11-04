__author__ = "730767778"

from find_max import find_and_remove_max


def test_main() -> None:
    nums: list[int] = [1, 6, 9, 7]
    assert find_and_remove_max(nums) == 9


def test_mutation() -> None:
    nums: list[int] = [3, 5, 1, 1, 4, 5]
    find_and_remove_max(nums)
    assert nums == [3, 1, 1, 4]


def test_unconventional() -> None:
    nums: list[int] = []
    assert find_and_remove_max(nums) == -1
