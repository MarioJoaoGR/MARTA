
import pytest
from unittest.mock import MagicMock, patch
from ansible.modules.iptables import insert_rule

def test_insert_rule_valid():
    mock_module = MagicMock()
    with patch('ansible.modules.iptables.push_arguments', return_value=['/usr/sbin/iptables', '-t', 'filter', '-I', 'INPUT']):
        insert_rule('/usr/sbin/iptables', mock_module, {'table': 'filter', 'chain': 'INPUT'})
        assert mock_module.run_command.called


def test_insert_rule_missing_params():
    mock_module = MagicMock()
    with pytest.raises(KeyError):
        insert_rule('/usr/sbin/iptables', mock_module, {'table': 'filter'})


def test_insert_rule_missing_table():
    mock_module = MagicMock()
    with pytest.raises(KeyError):
        insert_rule('/usr/sbin/iptables', mock_module, {'chain': 'INPUT'})