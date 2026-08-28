
import pytest
from unittest.mock import MagicMock
import re

# Import the function with its module name
from ansible.modules.iptables import get_chain_policy

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.params = {
        'table': 'filter',
        'chain': 'INPUT'
    }
    return module

# Test cases for get_chain_policy function
def test_get_chain_policy_basic(mock_module):
    mock_module.run_command.return_value = (0, "Chain INPUT (policy ACCEPT)\n", "")
    result = get_chain_policy('/usr/sbin/iptables', mock_module, {'table': 'filter', 'chain': 'INPUT'})
    assert result == 'ACCEPT'

def test_get_chain_policy_different_table(mock_module):
    mock_module.run_command.return_value = (0, "Chain PREROUTING (policy DROP)\n", "")
    result = get_chain_policy('/usr/sbin/iptables', mock_module, {'table': 'nat', 'chain': 'PREROUTING'})
    assert result == 'DROP'

def test_get_chain_policy_no_policy(mock_module):
    mock_module.run_command.return_value = (0, "Chain FORWARD (1 references)\n", "")
    result = get_chain_policy('/usr/sbin/iptables', mock_module, {'table': 'filter', 'chain': 'FORWARD'})
    assert result is None

def test_get_chain_policy_mock_module(mock_module):
    mock_module.run_command.return_value = (0, "Chain OUTPUT (policy DROP)\n", "")
    result = get_chain_policy('/usr/sbin/iptables', mock_module, {'table': 'filter', 'chain': 'OUTPUT'})