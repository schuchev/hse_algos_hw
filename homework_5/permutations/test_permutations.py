import pytest
from homework_5.permutations.permutations import permutations


def test_1():
    nums = [1,2,3]
    result = permutations(nums)
    expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    for perm in expected:
        assert perm in result
    assert len(result) == len(expected)

def test_2():
    nums = [0,1]
    result = permutations(nums)
    expected = [[0,1],[1,0]]
    for perm in expected:
        assert perm in result
    assert len(result) == len(expected)

def test_3():
    nums = [1]
    result = permutations(nums)
    expected = [[1]]
    assert result == expected

def test_4():
    nums = []
    result = permutations(nums)
    expected = [[]]
    assert result == expected
