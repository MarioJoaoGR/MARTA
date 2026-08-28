
import pytest
from ansible.module_utils.facts.collector import _solve_deps, find_unresolved_requires, resolve_requires


def test_invalid_input():
    collector_names = ['unknown']
    all_fact_subsets = {
        'cpu': frozenset({'a', 'b'}),
        'memory': frozenset({'c', 'd'}),
        'disk': frozenset({'e', 'f'})
    }
    
    with pytest.raises(KeyError):
        _solve_deps(collector_names, all_fact_subsets)