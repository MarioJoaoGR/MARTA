
import pytest
from ansible.module_utils.facts.collector import get_collector_names
from collections import defaultdict

# Test cases for get_collector_names function

def test_gather_all_exclude_hardware():
    result = get_collector_names(valid_subsets=frozenset(['all', 'network']), gather_subset=['!hardware'])
    assert set(['all', 'network']) == result, f"Expected all and network subsets, got {result}"

def test_minimal_plus_network():
    result = get_collector_names(valid_subsets=frozenset(['all', 'network']), minimal_gather_subset=frozenset(['min']), gather_subset=['network'])
    assert set(['min', 'network']) == result, f"Expected min and network subsets, got {result}"

def test_specific_subsets():
    result = get_collector_names(valid_subsets=frozenset(['all', 'network', 'memory']), gather_subset=['all', '!storage'])
    expected = set(['all', 'network', 'memory']) - set(['storage'])
    assert expected == result, f"Expected all and network plus memory but not storage, got {result}"

def test_aliases():
    aliases_map = defaultdict(set, {'hardware': ['cpu', 'memory']})
    result = get_collector_names(valid_subsets=frozenset(['all', 'network']), gather_subset=['!hardware'], aliases_map=aliases_map)
    expected = set(['all', 'network']) - set(['cpu', 'memory'])
    assert expected == result, f"Expected all and network but not cpu or memory, got {result}"

def test_no_specific_subset():
    result = get_collector_names(valid_subsets=frozenset(['all', 'network']))