
import pytest
from unittest.mock import patch, MagicMock
from ansible.playbook.play import Play





@patch('ansible.playbook.role.include.RoleInclude')
def test_play_serialize(mock_role_include):
    data = {
        'hosts': ['localhost'],
        'roles': ['role1', 'role2']
    }
    mock_role_include.return_value.serialize.side_effect = lambda: {'name': 'role1'}
    play = Play.load(data)
    serialized_data = play.serialize()
    assert 'hosts' in serialized_data
    assert 'roles' in serialized_data

