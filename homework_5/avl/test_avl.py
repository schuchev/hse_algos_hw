import pytest
from avl_ import AVL  

def test_1():
    tree = AVL()
    tree.add(10)
    tree.add(20)
    tree.add(5)
    assert tree.search(10)
    assert tree.search(5)
    assert tree.search(20)
    assert not tree.search(15)

def test_2():
    tree = AVL()
    for v in [10, 20, 5, 15]:
        tree.add(v)

    tree.remove(20)
    assert not tree.search(20)
    assert tree.search(10)
    tree.remove(5)
    assert not tree.search(5)
    assert tree.search(15)

def test_3():
    tree = AVL()
    nums = [30, 20, 40, 10, 25, 35, 50]
    for n in nums:
        tree.add(n)
    for n in [20, 30]:
        tree.remove(n)
    assert tree.search(25)
    assert tree.search(40)
    assert not tree.search(30)
