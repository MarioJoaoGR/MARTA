
import pytest
from ansible.module_utils.facts.collector import _solve_deps, find_unresolved_requires, resolve_requires, CollectorNotFoundError



def test_error_case():
    collector_names = ['cpu']
    all_fact_subsets = {'cpu': None}
    
    with pytest.raises(TypeError):
        _solve_deps(collector_names, all_fact_subsets)