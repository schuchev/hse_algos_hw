import pytest
from homework_10.kmp.kmp import kmp

def test_1():
    text = "ababcababcababc"
    pattern = "ababc"
    assert kmp(text, pattern) == [0, 5, 10]

def test_2():
    text = "abcdefg"
    pattern = "hij"
    assert kmp(text, pattern) == []

def test_3():
    text = "abc"
    pattern = "abcdef"
    assert kmp(text, pattern) == []

def test_4():
    text = "fffff"
    pattern = "f"
    assert kmp(text, pattern) == [0,1,2,3,4]

def test_5():
    text = "pattern"
    pattern = "pattern"
    assert kmp(text, pattern) == [0]

def test_6():
    text = "aaaa"
    pattern = "aa"
    assert kmp(text, pattern) == [0,1,2]
