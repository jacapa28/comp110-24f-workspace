"""Tests written for functions in utils.py"""

__author__ = "730767778"

from utils import only_evens, sub, add_at_index
from pytest import raises


def test_only_evens_edge() -> None:
    """Tests unusual case where no evens are found"""
    nums: list[int] = [3, 5, 7, 9]
    assert only_evens(nums) == []


def test_only_evens_main() -> None:
    """Detects for a few evens"""
    nums: list[int] = [1, 2, 2, 5, 8]
    assert only_evens(nums) == [2, 2, 8]


def test_only_evens_mutation() -> None:
    """Tests if input list has been mutated"""
    nums: list[int] = [1, 2, 2, 5, 8]
    only_evens(nums)
    assert nums == [1, 2, 2, 5, 8]


def test_sub_edge() -> None:
    """Tests unusual case where empty list should be returned"""
    nums: list[int] = [5, 10, 15, 20, 25]
    assert sub(nums, 6, -1) == []


def test_sub_main() -> None:
    """Tests standard case where normal sub list is returned"""
    nums: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    assert sub(nums, 2, 5) == [3, 4, 5]


def test_sub_mutation() -> None:
    """Tests that input list has not been mutated"""
    nums: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    sub(nums, 1, 7)
    assert nums == [1, 2, 3, 4, 5, 6, 7, 8]


def test_add_at_index_edge() -> None:
    """Tests case where index is at the very end"""
    nums: list[int] = [1, 2, 3, 4]
    with raises(IndexError):
        add_at_index(nums, 10, 10)


def test_add_at_index_main() -> None:
    """Tests standard case where a number is inputted in middle of list"""
    nums: list[int] = [5, 10, 15, 25, 30]
    add_at_index(nums, 20, 3)
    assert nums == [5, 10, 15, 20, 25, 30]


def test_add_at_index_mutation() -> None:
    """Tests case where there is an empty list and needs just one number added"""
    nums: list[int] = []
    add_at_index(nums, 0, 0)
    assert nums == [0]
