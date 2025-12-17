import pytest
from homework_10.lcs.lcs import lcs

def test_1():
    assert lcs("AGGTAB", "GXTXAYB") == "GTAB"

def test_2():
    assert lcs("ABC", "DEF") == ""

def test_3():
    assert lcs("ABC", "ABC") == "ABC"

def test_4():
    assert lcs("A", "A") == "A"

def test_5():
    assert lcs("aaaa", "aa") == "aa"

def test_6():
    assert lcs("", "") == ""
    assert lcs("ABC", "") == ""
    assert lcs("", "kwe") == ""
