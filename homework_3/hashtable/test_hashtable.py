import pytest
from hashtable import HashTable

def test_1():
    ht = HashTable()
    ht.insert("a", 10)
    ht.insert("b", 20)
    ht.insert("c", 30)
    assert ht.get("a") == 10
    assert ht.get("b") == 20
    assert ht.get("c") == 30

def test_2():
    ht = HashTable()
    ht.insert("a", 10)
    ht.insert("a", 50)
    assert ht.get("a") == 50

def test_3():
    ht = HashTable()
    ht.insert("a", 10)
    ht.insert("b", 20)
    ht.delete("a")
    with pytest.raises(KeyError):
        ht.get("a")
    assert ht.get("b") == 20

def test_4():
    ht = HashTable()
    with pytest.raises(KeyError):
        ht.delete("ff")

def test_5():
    ht = HashTable(capacity_initial=2, load_factor_initial=0.5)
    ht.insert("a", 1)
    ht.insert("b", 2)  
    ht.insert("c", 3)
    assert ht.get("a") == 1
    assert ht.get("b") == 2
    assert ht.get("c") == 3
