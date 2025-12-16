import pytest
from homework_9.components.component import find_connected_components 

def sort_components(components):
    return sorted([sorted(list(c)) for c in components])

def test_1():
    graph = {}
    res = find_connected_components(graph)
    assert sort_components(res) == []

def test_2():
    graph = {1: []}
    res = find_connected_components(graph)
    assert sort_components(res) == [[1]]

def test_3():
    graph = {1: [], 2: [], 3: []}
    res = find_connected_components(graph)
    expected = [[1], [2], [3]]
    assert sort_components(res) == sort_components(expected)

def test_3():
    graph = {
        1: [2, 3],
        2: [1],
        3: [1],
        4: [5],
        5: [4],
    }
    res = find_connected_components(graph)
    expected = [[1, 2, 3], [4, 5]]
    assert sort_components(res) == sort_components(expected)

def test_4():
    graph = {
        1: [2],
        2: [1],
        3: [],
        4: [5],
        5: [4],
        6: []
    }
    res = find_connected_components(graph)
    expected = [[1, 2], [3], [4, 5], [6]]
    assert sort_components(res) == sort_components(expected)

def test_5():
    graph = {
        1: [2],
        2: [3],
        3: [1],
        4: [5],
        5: [4]
    }
    res = find_connected_components(graph)
    expected = [[1, 2, 3], [4, 5]]
    assert sort_components(res) == sort_components(expected)
