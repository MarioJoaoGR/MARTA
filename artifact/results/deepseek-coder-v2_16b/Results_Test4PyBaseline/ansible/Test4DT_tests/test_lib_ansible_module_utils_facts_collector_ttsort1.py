
# Module: ansible.module_utils.facts.collector
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

def test_tsort_two_nodes():
    dep_map = {'a': ['b'], 'b': []}
    result = tsort(dep_map)
    assert result == [('b', []), ('a', ['b'])]

def test_tsort_three_nodes():
    dep_map = {'a': ['b'], 'b': ['c'], 'c': []}
    result = tsort(dep_map)
    assert result == [('c', []), ('b', ['c']), ('a', ['b'])]

def test_tsort_cycle():
    dep_map = {'a': ['b'], 'b': ['c'], 'c': ['a']}
    with pytest.raises(CycleFoundInFactDeps) as excinfo:
        tsort(dep_map)
    assert str(excinfo.value) == "Unable to tsort deps, there was a cycle in the graph. sorted=[]"
