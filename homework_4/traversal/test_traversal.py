import pytest
from traversal import BST

@pytest.fixture
def bst():
    root = BST(10)
    for val in [4, 2, 8, 15, 12, 18, 1, 3, 5]:
        root.insert(val)
    return root


def test_inorder(bst):
    assert bst.inorder() == [1, 2, 3, 4, 5, 8, 10, 12, 15, 18]


def test_preorder(bst):
    assert bst.preorder() == [10, 4, 2, 1, 3, 8, 5, 15, 12, 18]


def test_postorder(bst):
    assert bst.postorder() == [1, 3, 2, 5, 8, 4, 12, 18, 15, 10]


def test_reverse_inorder(bst):
    assert bst.reverse_inorder() == [18, 15, 12, 10, 8, 5, 4, 3, 2, 1]


def test_reverse_preorder(bst):
    assert bst.reverse_preorder() == [10, 15, 18, 12, 4, 8, 5, 2, 3, 1]


def test_reverse_postorder(bst):
    assert bst.reverse_postorder() == [18, 12, 15, 5, 8, 3, 1, 2, 4, 10]
