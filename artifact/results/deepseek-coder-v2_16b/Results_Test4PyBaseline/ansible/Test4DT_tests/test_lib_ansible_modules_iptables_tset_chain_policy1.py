
import pytest
from unittest.mock import MagicMock
from ansible.modules.iptables import set_chain_policy

@pytest.fixture
def mock_module():
    module = MagicMock()
    return module

# Test case to cover line 699: push_arguments usage and command construction
def test_set_chain_policy_command_construction(mock_module):
    params = {
        'table': 'filter',
        'chain': 'INPUT',
        'policy': 'DROP'
    }
    set_chain_policy('/usr/sbin/iptables', mock_module, params)
    expected_cmd = ['/usr/sbin/iptables', '-t', 'filter', '-P', 'INPUT', 'DROP']
    assert mock_module.run_command.call_args[0][0] == expected_cmd

# Test case to cover line 700: command appending the policy
def test_set_chain_policy_appending_policy(mock_module):
    params = {
        'table': 'filter',
        'chain': 'INPUT',
        'policy': 'DROP'
    }
    set_chain_policy('/usr/sbin/iptables', mock_module, params)
    expected_cmd = ['/usr/sbin/iptables', '-t', 'filter', '-P', 'INPUT', 'DROP']
    assert mock_module.run_command.call_args[0][0] == expected_cmd

# Test case to cover line 701: run_command with check_rc=True
def test_set_chain_policy_check_rc(mock_module):
    params = {
        'table': 'filter',
        'chain': 'INPUT',
        'policy': 'DROP'
    }
    set_chain_policy('/usr/sbin/iptables', mock_module, params)
    assert mock_module.run_command.call_args[1]['check_rc'] is True
