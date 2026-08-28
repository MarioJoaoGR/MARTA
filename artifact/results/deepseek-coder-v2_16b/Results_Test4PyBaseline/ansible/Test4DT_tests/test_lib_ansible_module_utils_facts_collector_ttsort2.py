
import pytest
from ansible.module_utils.facts.collector import tsort, CycleFoundInFactDeps

def test_tsort_empty_dep_map():
    dep_map = {}
    result = tsort(dep_map)
    assert result == []

def test_tsort_single_node():
    dep_map = {'a': []}
    result = tsort(dep_map)
    assert result == [('a', [])]

def test_tsort_no_dependencies():
    dep_map = {'a': [], 'b': [], 'c': []}
    result = tsort(dep_map)
    assert result == [('a', []), ('b', []), ('c', [])]

def test_tsort_large_graph():
    dep_map = {
        'a': ['b'],
        'b': ['c', 'd'],
        'c': [],
        'd': ['e'],
        'e': ['f'],
        'f': []
    }
    result = tsort(dep_map)
    assert result == [('c', []), ('f', []), ('e', ['f']), ('d', ['e']), ('b', ['c', 'd']), ('a', ['b'])]

def test_tsort_cyclic():
    dep_map = {'a': ['b'], 'b': ['c'], 'c': ['a']}
    with pytest.raises(CycleFoundInFactDeps) as excinfo:
        tsort(dep_map)
    assert str(excinfo.value) == "Unable to tsort deps, there was a cycle in the graph. sorted=[]"

def test_tsort_already_sorted():
    dep_map = {'a': ['b'], 'b': [], 'c': [], 'd': []}
    result = tsort(dep_map)