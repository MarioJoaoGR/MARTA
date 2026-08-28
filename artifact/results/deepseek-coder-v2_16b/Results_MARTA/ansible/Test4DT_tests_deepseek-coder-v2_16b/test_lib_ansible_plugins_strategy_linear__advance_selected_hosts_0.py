
import pytest
from unittest.mock import patch
from ansible.plugins.strategy.linear import _advance_selected_hosts

# Define a simple host object for testing
class Host:
    def __init__(self, name):
        self.name = name

# Define a noop task for testing
noop_task = "noop"

# Test data classes
host1 = Host("host1")
host2 = Host("host2")
host3 = Host("host3")

# Scenario 1: test_valid_input - Valid input with hosts, cur_block, and cur_state
def test_valid_input():
    hosts = [host1, host2, host3]
    cur_block = 1
    cur_state = 'running'
    result = _advance_selected_hosts(hosts, cur_block, cur_state)
    assert len(result) == 3, "Expected all three hosts to be processed"
    for (host, task) in result:
        assert isinstance(host, Host), f"Host should be an instance of Host but got {type(host)}"
        if host.name == 'host1':
            assert task == noop_task, "Expected host1 to have a noop task"
        elif host.name == 'host2':
            assert task == noop_task, "Expected host2 to have a noop task"
        elif host.name == 'host3':
            assert task == noop_task, "Expected host3 to have a noop task"

# Scenario 2: test_edge_case_no_hosts - No hosts provided
def test_edge_case_no_hosts():
    hosts = []
    cur_block = 1
    cur_state = 'running'
    result = _advance_selected_hosts(hosts, cur_block, cur_state)
    assert len(result) == 0, "Expected no hosts to be processed"

# Scenario 3: test_invalid_input - Invalid input where cur_state does not match any active task state
def test_invalid_input():
    hosts = [host1, host2, host3]
    cur_block = 1
    cur_state = 'stopped'
    result = _advance_selected_hosts(hosts, cur_block, cur_state)
    assert len(result) == 3, "Expected all three hosts to be processed"
    for (host, task) in result:
        assert isinstance(host, Host), f"Host should be an instance of Host but got {type(host)}"
        if host.name == 'host1':
            assert task == noop_task, "Expected host1 to have a noop task"
        elif host.name == 'host2':
            assert task == noop_task, "Expected host2 to have a noop task"
        elif host.name == 'host3':
            assert task == noop_task, "Expected host3 to have a noop task"
