
import pytest
from unittest.mock import patch, MagicMock
from ansible.inventory.host import Host


@patch('ansible.inventory.host.get_unique_id')
def test_host_equality_with_mocked_uuid(mock_get_unique_id):
    mock_get_unique_id.return_value = 'unique-uuid'
    host1 = Host(name='exampleHost', port=22, gen_uuid=True)
    host2 = Host(name='exampleHost', port=22, gen_uuid=True)
    assert host1 == host2

def test_host_inequality():
    host1 = Host(name='exampleHost1', port=22, gen_uuid=True)
    host2 = Host(name='exampleHost2', port=22, gen_uuid=True)
    assert host1 != host2

@patch('ansible.inventory.host.get_unique_id')
def test_host_inequality_with_mocked_uuid(mock_get_unique_id):
    mock_get_unique_id.side_effect = [ 'unique-uuid-1', 'unique-uuid-2' ]
    host1 = Host(name='exampleHost1', port=22, gen_uuid=True)
    host2 = Host(name='exampleHost2', port=22, gen_uuid=True)
    assert host1 != host2