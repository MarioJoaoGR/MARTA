
import pytest
from ansible.plugins.strategy import free

@pytest.fixture
def setup_valid_input():
    tqm = None  # Assuming tqm is a valid object representing the test quality manager
    strategy = free.StrategyModule(tqm)
    notified_hosts = ['host1', 'host2', 'host3']
    strategy._flushed_hosts = {'host1': True, 'host2': False, 'host3': True}
    return strategy, notified_hosts

@pytest.fixture
def setup_edge_case():
    tqm = None  # Assuming tqm is a valid object representing the test quality manager
    strategy = free.StrategyModule(tqm)
    notified_hosts = []
    strategy._flushed_hosts = {}
    return strategy, notified_hosts

@pytest.fixture
def setup_invalid_input():
    tqm = None  # Assuming tqm is a valid object representing the test quality manager
    strategy = free.StrategyModule(tqm)
    notified_hosts = None
    return strategy, notified_hosts

def test_valid_input(setup_valid_input):
    strategy, notified_hosts = setup_valid_input
    filtered_hosts = strategy._filter_notified_hosts(notified_hosts)
    assert len(filtered_hosts) == 2
    assert 'host1' in filtered_hosts
    assert 'host3' in filtered_hosts

def test_edge_case(setup_edge_case):
    strategy, notified_hosts = setup_edge_case
    filtered_hosts = strategy._filter_notified_hosts(notified_hosts)
    assert len(filtered_hosts) == 0

def test_invalid_input(setup_invalid_input):
    strategy, notified_hosts = setup_invalid_input
    with pytest.raises(TypeError):
        filtered_hosts = strategy._filter_notified_hosts(notified_hosts)
