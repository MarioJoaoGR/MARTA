# Module: ansible.plugins.strategy.linear
import pytest
from ansible.plugins.strategy.linear import _advance_selected_hosts

# Test Case 1: Basic Usage
def test_basic_usage():
    hosts = [
        {'name': 'host1', 'task': {'state': 'running'}},
        {'name': 'host2', 'task': {'state': 'pending'}}
    ]
    advanced_hosts = _advance_selected_hosts(hosts, 1, 'running')
    assert len(advanced_hosts) == 1
    assert advanced_hosts[0][0]['name'] == 'host1'
    assert advanced_hosts[0][1] is not None

# Test Case 2: Handling Noop Tasks
def test_handle_noop_tasks():
    hosts = [
        {'name': 'host1', 'task': {'state': 'completed'}},
        {'name': 'host2', 'task': {'state': 'running'}}
    ]
    advanced_hosts = _advance_selected_hosts(hosts, 1, 'running')
    assert len(advanced_hosts) == 1
    assert advanced_hosts[0][0]['name'] == 'host2'
    assert advanced_hosts[0][1] is not None

# Test Case 3: Handling No Hosts in the Requested State
def test_no_hosts_in_requested_state():
    hosts = [
        {'name': 'host1', 'task': {'state': 'completed'}},
        {'name': 'host2', 'task': {'state': 'failed'}}
    ]
    advanced_hosts = _advance_selected_hosts(hosts, 1, 'running')
    assert len(advanced_hosts) == 0

# Test Case 4: Using Different Block and State Numbers
def test_different_block_and_state():
    hosts = [
        {'name': 'host1', 'task': {'state': 'running'}},
        {'name': 'host2', 'task': {'state': 'pending'}}
    ]
    advanced_hosts = _advance_selected_hosts(hosts, 2, 'failed')
    assert len(advanced_hosts) == 1
    assert advanced_hosts[0][0]['name'] == 'host1'
    assert advanced_hosts[0][1] is not None
