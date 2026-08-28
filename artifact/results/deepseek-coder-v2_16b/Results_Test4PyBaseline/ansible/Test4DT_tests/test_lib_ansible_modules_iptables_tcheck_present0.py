# Module: ansible.modules.iptables
import pytest
from unittest.mock import MagicMock

# Import the function to be tested
from ansible.modules.iptables import check_present

@pytest.fixture
def mock_module():
    module = MagicMock()
    return module

@pytest.mark.parametrize("params, expected", [
    ({'table': 'filter', 'chain': 'INPUT', 'rule_num': '1'}, True),
    ({'table': 'nat', 'chain': 'PREROUTING', 'rule_num': '1'}, False),
])
def test_check_present(mock_module, params, expected):
    # Mock the module to return a specific command result
    mock_module.run_command = MagicMock()
    if expected:
        mock_module.run_command.return_value = (0, "Rule found\n", "")
    else:
        mock_module.run_command.return_value = (1, "Rule not found\n", "")
    
    # Call the function with mocked module and parameters
    result = check_present('/usr/sbin/iptables', mock_module, params)
    
    # Assert that the command was run correctly and returned the expected result
    assert result == expected
