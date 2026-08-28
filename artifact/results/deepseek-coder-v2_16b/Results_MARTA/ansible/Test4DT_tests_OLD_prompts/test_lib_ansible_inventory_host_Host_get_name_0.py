
import pytest
from unittest.mock import patch, MagicMock
from ansible.inventory.host import Host

# Test Scenario 1: test_valid_input
def test_valid_input():
    with patch('ansible.inventory.host.get_unique_id', return_value='unique_id'):
        host = Host(name='exampleHost', port=22)
        assert host.name == 'exampleHost'
        assert host.vars['ansible_port'] == 22
        assert host._uuid == 'unique_id'

# Test Scenario 2: test_edge_case
def test_edge_case():
    with patch('ansible.inventory.host.get_unique_id', return_value='unique_id'):
        host = Host(name=None, port=None, gen_uuid=False)
        assert host.name is None
        assert 'ansible_port' not in host.vars
        assert host._uuid is None

# Test Scenario 3: test_invalid_input
def test_invalid_input():
    with patch('ansible.inventory.host.get_unique_id', return_value='unique_id'):
        with pytest.raises(ValueError):
            host = Host(name='exampleHost', port='invalid_port', gen_uuid=True)
