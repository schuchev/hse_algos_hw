import pytest
from homework_6.kth.kth_ import quickselect 

def test_1():
    nums = [3,2,1,5,6,4]
    assert quickselect(nums, 2) == 5
    assert quickselect(nums, 1) == 6
    assert quickselect(nums, 6) == 1

def test_2():
    nums = [3,2,3,1,2,4,5,5,6]
    assert quickselect(nums, 4) == 4
    assert quickselect(nums, 1) == 6
    assert quickselect(nums, 9) == 1

def test_3():
    nums = [7,7,7,7,7]
    assert quickselect(nums, 1) == 7
    assert quickselect(nums, 3) == 7
    assert quickselect(nums, 5) == 7

def test_4():
    nums = [34]
    assert quickselect(nums, 1) == 34
