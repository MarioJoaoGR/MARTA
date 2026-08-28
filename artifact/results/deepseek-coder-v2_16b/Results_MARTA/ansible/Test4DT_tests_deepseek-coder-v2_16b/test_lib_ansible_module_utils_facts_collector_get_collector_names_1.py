
import pytest
from ansible.module_utils.facts.collector import get_collector_names

def test_valid_case_all_subsets():
    result = get_collector_names(valid_subsets=frozenset(['all', 'network']), gather_subset=['all'])
    assert set(result) == {'all', 'network'}

def test_edge_case_none_input():
    with pytest.raises(TypeError):
        result = get_collector_names()

def test_invalid_case_unknown_subset():
    with pytest.raises(TypeError):
        result = get_collector_names(valid_subsets=frozenset(['all', 'network']), gather_subset=['!hardware', 'network'])
