
import pytest
from ansible.playbook.play import Play

# Test valid input scenario
def test_valid_input():
    datastructure = {
        'hosts': ['localhost'],
        'roles': ['webserver', 'database']
    }
    play = Play.load(datastructure)
    
    assert isinstance(play, Play), "Expected an instance of Play"
    assert play._hosts == ['localhost'], "Expected hosts to be ['localhost']"
    assert play._roles == ['webserver', 'database'], "Expected roles to be ['webserver', 'database']"

# Test edge case scenario with None input
def test_edge_case():
    datastructure = None
    with pytest.raises(TypeError):
        Play.load(datastructure)

# Test invalid input scenario
def test_invalid_input():
    datastructure = {
        'hosts': 123,  # Invalid type for hosts
        'roles': ['webserver', 'database']
    }
    with pytest.raises(TypeError):
        Play.load(datastructure)
