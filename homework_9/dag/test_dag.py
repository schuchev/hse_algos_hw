import pytest
from homework_9.dag.dag import detect_cycle_and_toposort

def test_1():
    graph = {
        1: [2, 3],
        2: [4],
        3: [4],
        4: []
    }
    has_cycle, topo = detect_cycle_and_toposort(graph)
    assert has_cycle == False
    assert set(topo) == {1, 2, 3, 4}
    assert topo.index(1) < topo.index(2)
    assert topo.index(1) < topo.index(3)
    assert topo.index(2) < topo.index(4)
    assert topo.index(3) < topo.index(4)

def test_2():
    graph = {
        1: [2],
        2: [3],
        3: [1]
    }
    has_cycle, cycle = detect_cycle_and_toposort(graph)
    assert has_cycle == True
    assert cycle[0] == cycle[-1]
    assert set(cycle[:-1]).issubset({1, 2, 3})

def test_3():
    graph = {
        1: [2],
        2: [],
        3: [4],
        4: []
    }
    has_cycle, topo = detect_cycle_and_toposort(graph)
    assert has_cycle == False
    assert set(topo) == {1, 2, 3, 4}
    assert topo.index(1) < topo.index(2)
    assert topo.index(3) < topo.index(4)

def test_4():
    graph = {1: []}
    has_cycle, topo = detect_cycle_and_toposort(graph)
    assert has_cycle == False
    assert topo == [1]

def test_5():
    graph = {1: [1]}
    has_cycle, cycle = detect_cycle_and_toposort(graph)
    assert has_cycle == True
    assert cycle == [1, 1]
