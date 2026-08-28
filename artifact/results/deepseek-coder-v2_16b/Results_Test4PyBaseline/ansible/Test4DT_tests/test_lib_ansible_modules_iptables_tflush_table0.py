# Module: ansible.modules.iptables
import pytest
from ansible.modules.iptables import flush_table
from unittest.mock import MagicMock

# Mock the necessary parts of Ansible's Module class for testing
class MockModule:
    def __init__(self):
        self.run_command = MagicMock()

# Test cases for flush_table function
def test_flush_table_basic():
    iptables_path = '/usr/sbin/iptables'
    module = MockModule()
    params = {
        'table': 'filter',
        'chain': 'INPUT'
    }
    flush_table(iptables_path, module, params)
    # Assert that run_command was called with the correct command
    expected_cmd = ['/usr/sbin/iptables', '-F', '--table=filter', '--chain=INPUT']
    module.run_command.assert_called_with(' '.join(expected_cmd), check_rc=True)

def test_flush_table_default_values():
    iptables_path = '/usr/sbin/iptables'
    module = MockModule()
    params = {
        'chain': 'INPUT'  # Missing 'table' key, should default to 'filter'
    }
    flush_table(iptables_path, module, params)
    expected_cmd = ['/usr/sbin/iptables', '-F', '--table=filter', '--chain=INPUT']
    module.run_command.assert_called_with(' '.join(expected_cmd), check_rc=True)

def test_flush_table_hardcoded_values():
    iptables_path = '/usr/sbin/iptables'
    module = MockModule()
    params = {
        'table': 'filter',
        'chain': 'INPUT'
    }
    flush_table(iptables_path, module, params)
    expected_cmd = ['/usr/sbin/iptables', '-F', '--table=filter', '--chain=INPUT']
    module.run_command.assert_called_with(' '.join(expected_cmd), check_rc=True)
