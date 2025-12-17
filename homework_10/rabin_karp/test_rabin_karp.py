import pytest
from homework_10.rabin_karp.rabin_karp import rabin_karp

def test_1():
    assert rabin_karp("rfokwfwnvew", "okw") == 2
    assert rabin_karp("pevrorfrkv", "pev") == 0
    assert rabin_karp("wefwekfv", "fv") == 6
    assert rabin_karp("wefwekfv", "i") == -1

def test_2():
    assert rabin_karp("fwefowvm", "") == 0

def test_3():
    assert rabin_karp("abc", "abcd") == -1

def test_4():
    assert rabin_karp("dfe dwdwd", "wd") == 5

def test_5():
    assert rabin_karp("aaaaa", "aa") == 0
