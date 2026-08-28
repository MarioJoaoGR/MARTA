
import pytest
from ansible.playbook.play import Play

def test_valid_input():
    play_config = {
        'hosts': ['localhost'],
        'roles': ['role1', 'role2']
    }
    play = Play.load(play_config)
    
    assert play._hosts == ['localhost']
    assert play._gather_facts is None
    assert play._roles == ['role1', 'role2']

def test_edge_case():
    play_config = {
        'hosts': None,
        'roles': None
    }
    with pytest.raises(TypeError):
        Play.load(play_config)

def test_invalid_input():
    with pytest.raises(TypeError):
        Play()
