
import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.strategy.free import StrategyModule

# Test Scenario 1: test_valid_input
def test_valid_input():
    tqm = MagicMock()
    strategy = StrategyModule(tqm)
    notified_hosts = ['host1', 'host2', 'host3']
    strategy._flushed_hosts = {'host1': True, 'host2': False, 'host3': True}
    
    filtered_hosts = strategy._filter_notified_hosts(notified_hosts)
    assert set(filtered_hosts) == {'host1', 'host3'}

# Test Scenario 2: test_edge_case
def test_edge_case():
    tqm = MagicMock()
    strategy = StrategyModule(tqm)
    notified_hosts = []
    strategy._flushed_hosts = {}
    
    filtered_hosts = strategy._filter_notified_hosts(notified_hosts)
    assert len(filtered_hosts) == 0

# Test Scenario 3: test_invalid_input
def test_invalid_input():
    tqm = MagicMock()
    strategy = StrategyModule(tqm)
    notified_hosts = None
    strategy._flushed_hosts = {'host1': True, 'host2': False}
    
    with pytest.raises(TypeError):
        filtered_hosts = strategy._filter_notified_hosts(notified_hosts)
