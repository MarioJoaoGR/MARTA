
import pytest
from ansible.module_utils.facts.collector import get_collector_names


def test_get_collector_names_default():
    valid_subsets = frozenset(['all', 'network'])
    gather_subset = []
    result = get_collector_names(valid_subsets=valid_subsets, gather_subset=gather_subset)
    assert set(result) == {'all', 'network'}
