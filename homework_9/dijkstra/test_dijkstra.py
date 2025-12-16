import pytest
from homework_9.dijkstra.dijkstra import dijkstra

def test_1():
    graph = {
        1: [(2, 4), (3, 2)],
        2: [(1, 4), (3, 5), (4, 10)],
        3: [(1, 2), (2, 5), (4, 3)],
        4: [(2, 10), (3, 3)]
    }
    result = dijkstra(graph, 1)
    expected = {1: 0, 2: 4, 3: 2, 4: 5}
    assert result == expected

def test_2():
    graph = {
        1: [(2, 1)],
        2: [(1, 1)],
        3: [],
        4: []
    }
    result = dijkstra(graph, 1)
    expected = {1: 0, 2: 1, 3: float('inf'), 4: float('inf')}
    assert result == expected

def test_3():
    graph = {1: []}
    result = dijkstra(graph, 1)
    expected = {1: 0}
    assert result == expected

def test_4():
    graph = {
        1: [(2, 0), (3, 1)],
        2: [(3, 0)],
        3: []
    }
    result = dijkstra(graph, 1)
    expected = {1: 0, 2: 0, 3: 0}
    assert result == expected

def test_5():
    graph = {
        1: [(2, 1)],
        2: [(3, 1)],
        3: [(1, 1)]
    }
    result = dijkstra(graph, 1)
    expected = {1: 0, 2: 1, 3: 2}
    assert result == expected
