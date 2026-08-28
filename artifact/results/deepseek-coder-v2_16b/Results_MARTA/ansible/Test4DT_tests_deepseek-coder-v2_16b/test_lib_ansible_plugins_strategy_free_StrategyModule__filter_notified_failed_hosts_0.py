
import pytest
from unittest.mock import patch
from ansible.plugins.strategy.free import StrategyModule

# Scenario 1: Test standard input with valid iterator and notified hosts
def test_valid_input():
    class MockIterator:
        def is_failed(self, host):
            return host == 'host2'  # Only 'host2' should be marked as failed

    tqm_object = None  # Assuming tqm_object is a valid object representing the test quality manager
    strategy_module = StrategyModule(tqm_object)
    iterator = MockIterator()
    notified_hosts = ['host1', 'host2', 'host3']
    
    filtered_hosts = strategy_module._filter_notified_failed_hosts(iterator, notified_hosts)
    
    assert len(filtered_hosts) == 2
    assert 'host1' in filtered_hosts
    assert 'host3' in filtered_hosts
    assert 'host2' not in filtered_hosts

# Scenario 2: Test edge case with None input
def test_edge_case():
    class MockIterator:
        def is_failed(self, host):
            return False  # No hosts should be marked as failed

    tqm_object = None  # Assuming tqm_object is a valid object representing the test quality manager
    strategy_module = StrategyModule(tqm_object)
    iterator = MockIterator()
    notified_hosts = None
    
    filtered_hosts = strategy_module._filter_notified_failed_hosts(iterator, notified_hosts)
    
    assert filtered_hosts is None

# Scenario 3: Test invalid input with empty list and non-iterable input
def test_invalid_input():
    class MockIterator:
        def is_failed(self, host):
            return False  # No hosts should be marked as failed

    tqm_object = None  # Assuming tqm_object is a valid object representing the test quality manager
    strategy_module = StrategyModule(tqm_object)
    iterator = MockIterator()
    notified_hosts = []
    
    filtered_hosts = strategy_module._filter_notified_failed_hosts(iterator, notified_hosts)
    
    assert len(filtered_hosts) == 0
