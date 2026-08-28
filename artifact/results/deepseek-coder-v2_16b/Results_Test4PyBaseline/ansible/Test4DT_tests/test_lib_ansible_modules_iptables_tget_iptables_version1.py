
import pytest
from unittest.mock import MagicMock

# Import the function from the specified module
from ansible.modules.iptables import get_iptables_version

@pytest.fixture
def mock_module():
    module = MagicMock()
    return module

# Test case to cover line 715 (command execution)
def test_get_iptables_version_command_execution(mock_module):
    iptables_path = '/usr/sbin/iptables'
    mock_module.run_command.return_value = (0, 'iptables v1.8.7\n', '')
    version = get_iptables_version(iptables_path, mock_module)
    assert version == '1.8.7'
    mock_module.run_command.assert_called_once_with([iptables_path, '--version'], check_rc=True)

# Test case to cover line 716 (successful command execution with valid output)
def test_get_iptables_version_valid_output(mock_module):
    iptables_path = '/usr/sbin/iptables'
    mock_module.run_command.return_value = (0, 'iptables v2.0.0\n', '')
    version = get_iptables_version(iptables_path, mock_module)