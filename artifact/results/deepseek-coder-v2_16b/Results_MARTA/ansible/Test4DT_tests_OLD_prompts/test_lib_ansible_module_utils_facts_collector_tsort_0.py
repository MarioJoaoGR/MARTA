
import pytest
from unittest.mock import patch
from ansible.module_utils.facts.collector import tsort, CycleFoundInFactDeps

def test_valid_input():
    dep_map = {'A': ['B'], 'B': [], 'C': ['A']}
    with patch('ansible.module_utils.facts.collector.tsort', side_effect=lambda x: list(x.items())):
        sorted_list = tsort(dep_map)
        assert sorted_list == [('B', []), ('A', ['B']), ('C', ['A'])]

def test_empty_input():
    dep_map = {}
    with patch('ansible.module_utils.facts.collector.tsort', side_effect=lambda x: list(x.items())):
        sorted_list = tsort(dep_map)
        assert sorted_list == []

def test_cycle_input():
    dep_map = {'A': ['B'], 'B': ['C'], 'C': ['A']}
    with patch('ansible.module_utils.facts.collector.tsort', side_effect=lambda x: list(x.items())):
        with pytest.raises(CycleFoundInFactDeps):
            tsort(dep_map)
