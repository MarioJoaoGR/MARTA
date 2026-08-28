
import pytest
from ansible.module_utils.facts.collector import _solve_deps

def test_valid_input():
    collector_names = ['cpu', 'memory']
    all_fact_subsets = {
        'cpu': frozenset({'a', 'b'}),
        'memory': frozenset({'c', 'd'}),
        'disk': frozenset({'e', 'f'})
    }
    
    resolved_collectors = _solve_deps(collector_names, all_fact_subsets)
    assert set(resolved_collectors) == {'cpu', 'memory'}

def test_edge_case():
    collector_names = []
    all_fact_subsets = {}
    
    resolved_collectors = _solve_deps(collector_names, all_fact_subsets)
    assert set(resolved_collectors) == set()

def test_invalid_input():
    collector_names = None
    all_fact_subsets = None
    
    with pytest.raises(TypeError):
        _solve_deps(collector_names, all_fact_subsets)
