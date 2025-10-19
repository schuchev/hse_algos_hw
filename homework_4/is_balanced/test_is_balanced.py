import pytest
from is_balanced import TreeNode, is_balanced

def test_1():
    assert is_balanced(None) == True

def test_2():
    node = TreeNode(10)
    assert is_balanced(node) == True

def test_3():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert is_balanced(root) == True

def test_4():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    assert is_balanced(root) == False

def test_5():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    assert is_balanced(root) == False

def test_6():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(5)
    assert is_balanced(root) == False

def test_7():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = None
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = None
    assert is_balanced(root) == True
