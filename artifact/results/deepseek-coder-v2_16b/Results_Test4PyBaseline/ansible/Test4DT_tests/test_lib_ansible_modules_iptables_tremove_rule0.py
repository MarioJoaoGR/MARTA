# Module: ansible.modules.iptables
import pytest
from unittest.mock import MagicMock

# Import the function to be tested
from ansible.modules.iptables import remove_rule

@pytest.fixture
def mock_module():
    module = MagicMock()
    return module

@pytest.mark.parametrize("iptables_path, params", [
    ('/usr/sbin/iptables', {'table': 'filter', 'chain': 'INPUT', 'rule_num': 1}),
    ('/usr/sbin/iptables', {'table': 'nat', 'chain': 'PREROUTING', 'rule_num': 2}),
    ('/path/to/custom/iptables', {'table': 'filter', 'chain': 'FORWARD', 'rule_num': 1})
])
def test_remove_rule(mock_module, iptables_path, params):
    # Mock the run_command method to simulate command execution
    mock_module.run_command = MagicMock()
    
    remove_rule(iptables_path, mock_module, params)
    
    expected_cmd = f"{iptables_path} -D {params['chain']} {params['rule_num']}"
    mock_module.run_command.assert_called_with(expected_cmd, check_rc=True)
