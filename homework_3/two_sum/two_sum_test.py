import pytest
from two_sum import two_sum  

def test_1():
    assert two_sum([1, 3, 4, 10], 7) == (1, 2)
    assert two_sum([5, 5, 1, 4], 10) == (0, 1)


def test_2():
    assert two_sum([-1, -2, -3, -4], -5) == (1, 2)
    assert two_sum([-1, 2, 3], 1) == (0, 1)


def test_3():
    assert two_sum([0, 4, 5, 6], 5) == (0, 2)
    assert two_sum([0, 0, 1, 2], 0) == (0, 1)


def test_4():
    assert two_sum([2, 2, 3, 3], 4) == (0, 1)
    assert two_sum([1, 2, 6, 2, 4], 4) == (1, 3)
    assert two_sum([1000000, 500000, 1500000], 2000000) == (1, 2)
    assert two_sum([10, 1, 2, 3, 7], 17) == (0, 4)


