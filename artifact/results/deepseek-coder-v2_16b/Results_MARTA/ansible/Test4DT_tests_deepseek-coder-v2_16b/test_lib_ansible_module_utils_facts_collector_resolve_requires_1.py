
import pytest
from ansible.module_utils.facts.collector import resolve_requires, UnresolvedFactDep


def test_resolve_requires_failure():
    unresolved_requires = ['x', 'y', 'z']
    all_fact_subsets = {frozenset({'a', 'b'}), frozenset({'c'})}
    
    with pytest.raises(UnresolvedFactDep):
        resolve_requires(unresolved_requires, all_fact_subsets)

def test_resolve_requires_empty_all_fact_subsets():
    unresolved_requires = ['a', 'b', 'c']
    all_fact_subsets = set()
    
    with pytest.raises(UnresolvedFactDep):
        resolve_requires(unresolved_requires, all_fact_subsets)
