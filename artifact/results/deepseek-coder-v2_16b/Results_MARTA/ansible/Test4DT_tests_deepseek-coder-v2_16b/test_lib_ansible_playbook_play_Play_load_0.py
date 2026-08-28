
import pytest
from ansible.playbook.play import Play

# Test for valid input scenario
def test_valid_input():
    data = {
        'hosts': ['localhost'],
        'roles': ['role1', 'role2']
    }
    play = Play.load(data)
    
    assert isinstance(play, Play)
    assert play._hosts == ['localhost']
    assert play._roles == ['role1', 'role2']
    assert play._gather_facts is None

# Test for edge case scenario with empty lists and boundary values
def test_edge_case():
    data = {
        'hosts': [],
        'roles': []
    }
    play = Play.load(data)
    
    assert isinstance(play, Play)
    assert play._hosts == []
    assert play._roles == []
    assert play._gather_facts is None

# Test for invalid input scenario that should raise exceptions
def test_invalid_input():
    data = None
    with pytest.raises(TypeError):
        Play.load(data)
