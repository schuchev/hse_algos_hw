from validate_bst import BST,is_bst_valid
import pytest

def test_1():
    assert is_bst_valid(None) == True

def test_2():
    node = BST(10)
    assert is_bst_valid(node) == True

def test_3():
    root = BST(10)
    for val in [5, 15, 3, 7, 12, 18]:
        root.insert(val)
    assert is_bst_valid(root) == True

def test_4():
    root = BST(10)
    for val in [5, 15, 3, 7, 12, 18]:
        root.insert(val)
    root.left.right.val = 20 
    assert is_bst_valid(root) == False

def test_5():
    root = BST(10)
    root.left = BST(15)
    assert is_bst_valid(root) == False

def test_6():
    root = BST(10)
    root.right = BST(5)
    assert is_bst_valid(root) == False

def test_7():
    root = BST(10)
    root.left = BST(5)
    root.right = BST(15)
    root.left.right = BST(12) 
    assert is_bst_valid(root) == False

def test_8():
    root = BST(10)
    root.insert(5)
    root.insert(10)  
    assert is_bst_valid(root) == True
