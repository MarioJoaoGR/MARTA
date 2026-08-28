# Module: ansible.modules.iptables
# test_append_rule.py
from ansible.modules.iptables import append_rule
import pytest

@pytest.fixture
def mock_module():
    class MockModule:
        def __init__(self):
            self.run_command_calls = []
        
        def run_command(self, cmd, check_rc=True):
            self.run_command_calls.append(cmd)
    
    return MockModule()

def test_append_rule_basic(mock_module):
    params = {
        'table': 'filter',
        'chain': 'INPUT'
    }
    append_rule('/usr/sbin/iptables', mock_module, params)
    assert len(mock_module.run_command_calls) == 1
    expected_cmd = ['/usr/sbin/iptables', '-A', '-t', 'filter', '-C', 'INPUT']
    assert mock_module.run_command_calls[0] == expected_cmd

def test_append_rule_custom_table(mock_module):
    params = {
        'table': 'nat',
        'chain': 'OUTPUT'
    }
    append_rule('/usr/sbin/iptables', mock_module, params)
    assert len(mock_module.run_command_calls) == 1
    expected_cmd = ['/usr/sbin/iptables', '-A', '-t', 'nat', '-C', 'OUTPUT']
    assert mock_module.run_command_calls[0] == expected_cmd

def test_append_rule_custom_chain(mock_module):
    params = {
        'table': 'filter',
        'chain': 'FORWARD'
    }
    append_rule('/usr/sbin/iptables', mock_module, params)
    assert len(mock_module.run_command_calls) == 1
    expected_cmd = ['/usr/sbin/iptables', '-A', '-t', 'filter', '-C', 'FORWARD']
    assert mock_module.run_command_calls[0] == expected_cmd
