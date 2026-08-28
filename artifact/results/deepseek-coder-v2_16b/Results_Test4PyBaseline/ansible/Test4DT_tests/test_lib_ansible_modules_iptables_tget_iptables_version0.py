
import pytest
from unittest.mock import MagicMock

# Import the function from the specified module
from ansible.modules.iptables import get_iptables_version

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.run_command.return_value = (0, 'iptables v1.8.7\n', '')
    return module

def test_get_iptables_version(mock_module):
    iptables_path = '/usr/sbin/iptables'
    version = get_iptables_version(iptables_path, mock_module)
    assert version == '1.8.7'

def test_get_iptables_version_with_different_output(mock_module):
    mock_module.run_command.return_value = (0, 'iptables v2.0.0\n', '')
    iptables_path = '/usr/sbin/iptables'
    version = get_iptables_version(iptables_path, mock_module)
    assert version == '2.0.0'

def test_get_iptables_version_with_invalid_command():
    with pytest.raises(TypeError):
        get_iptables_version('/usr/sbin/iptables', None)
