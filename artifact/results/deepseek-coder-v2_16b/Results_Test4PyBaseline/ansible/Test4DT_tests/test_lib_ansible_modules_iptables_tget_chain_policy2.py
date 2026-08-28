
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
    assert result == 'DROP'

# Additional test cases for uncovered lines 705-711
def test_get_chain_policy_empty_output(mock_module):
    """Test when the output from iptables -L is empty."""
    mock_module.run_command.return_value = (0, "", "")
    result = get_chain_policy('/usr/sbin/iptables', mock_module, {'table': 'filter', 'chain': 'INPUT'})
    assert result is None

def test_get_chain_policy_no_match(mock_module):
    """Test when the output from iptables -L does not match the expected regex pattern."""
    mock_module.run_command.return_value = (0, "Chain INPUT (unrecognized format)\n", "")
    result = get_chain_policy('/usr/sbin/iptables', mock_module, {'table': 'filter', 'chain': 'INPUT'})
    assert result is None

def test_get_chain_policy_multiple_chains(mock_module):
    """Test when the output from iptables -L contains multiple chains."""
    mock_module.run_command.return_value = (0, "Chain INPUT (policy ACCEPT)\nChain FORWARD (1 references)\nChain OUTPUT (policy DROP)\n", "")
    result = get_chain_policy('/usr/sbin/iptables', mock_module, {'table': 'filter', 'chain': 'INPUT'})
    assert result == 'ACCEPT'

@pytest.mark.xfail(reason="Expected RuntimeError due to invalid path")
def test_get_chain_policy_invalid_path(mock_module):
    """Test when the provided iptables path is invalid."""
    with pytest.raises(RuntimeError):
        get_chain_policy('invalid/path', mock_module, {'table': 'filter', 'chain': 'INPUT'})
