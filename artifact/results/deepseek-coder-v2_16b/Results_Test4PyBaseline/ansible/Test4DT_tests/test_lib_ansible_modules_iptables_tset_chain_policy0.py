# Module: ansible.modules.iptables
import pytest
from unittest.mock import MagicMock

# Import the function from the specified module
from ansible.modules.iptables import set_chain_policy

@pytest.fixture
def mock_module():
    module = MagicMock()
    return module

def test_set_chain_policy_basic(mock_module):
    params = {
        'table': 'filter',
        'chain': 'INPUT',
        'policy': 'DROP'
    }
    set_chain_policy('/usr/sbin/iptables', mock_module, params)
    expected_cmd = ['/usr/sbin/iptables', '-P', 'INPUT', 'DROP']
    mock_module.run_command.assert_called_with(expected_cmd, check_rc=True)

def test_set_chain_policy_different_policy(mock_module):
    params = {
        'table': 'filter',
        'chain': 'INPUT',
        'policy': 'ACCEPT'
    }
    set_chain_policy('/usr/sbin/iptables', mock_module, params)
    expected_cmd = ['/usr/sbin/iptables', '-P', 'INPUT', 'ACCEPT']
    mock_module.run_command.assert_called_with(expected_cmd, check_rc=True)

def test_set_chain_policy_mock_module(mock_module):
    params = {
        'table': 'filter',
        'chain': 'INPUT',
        'policy': 'DROP'
    }
    set_chain_policy('/usr/sbin/iptables', mock_module, params)
    expected_cmd = ['/usr/sbin/iptables', '-P', 'INPUT', 'DROP']
    mock_module.run_command.assert_called_with(expected_cmd, check_rc=True)
