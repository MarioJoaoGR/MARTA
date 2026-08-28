# Module: ansible.modules.iptables
import pytest
from unittest.mock import MagicMock
from ansible.modules.iptables import insert_rule

# Mock the module object with a run_command method
module = MagicMock()

def test_insert_rule_basic():
    params = {
        'table': 'filter',
        'chain': 'INPUT',
        'rule_num': '1'
    }
    insert_rule('/usr/sbin/iptables', module, params)
    expected_cmd = ['/usr/sbin/iptables', '-I', 'INPUT', '1']
    module.run_command.assert_called_with(expected_cmd, check_rc=True)

def test_insert_rule_custom_chain():
    custom_params = {
        'table': 'nat',
        'chain': 'PREROUTING',
        'rule_num': '1'
    }
    insert_rule('/usr/sbin/iptables', module, custom_params)
    expected_cmd = ['/usr/sbin/iptables', '-I', 'PREROUTING', '1']
    module.run_command.assert_called_with(expected_cmd, check_rc=True)

def test_insert_rule_custom_position():
    params = {
        'table': 'filter',
        'chain': 'INPUT',
        'rule_num': '2'
    }
    insert_rule('/usr/sbin/iptables', module, params)
    expected_cmd = ['/usr/sbin/iptables', '-I', 'INPUT', '2']
    module.run_command.assert_called_with(expected_cmd, check_rc=True)

def test_insert_rule_custom_table():
    custom_params = {
        'table': 'nat',
        'chain': 'PREROUTING',
        'rule_num': '1'
    }
    insert_rule('/usr/sbin/iptables', module, custom_params)
    expected_cmd = ['/usr/sbin/iptables', '-I', 'PREROUTING', '1']
    module.run_command.assert_called_with(expected_cmd, check_rc=True)
