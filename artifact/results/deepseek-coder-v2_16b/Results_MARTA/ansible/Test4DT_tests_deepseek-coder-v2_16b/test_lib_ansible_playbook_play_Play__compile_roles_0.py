
import pytest
from ansible.playbook.play import Play

# Test valid input scenario
def test_valid_input():
    datastructure = {
        'hosts': ['localhost'],
        'gather_facts': True,
        'roles': ['webserver', 'database']
    }
    play = Play.load(datastructure)
    
    assert isinstance(play, Play), "Expected an instance of Play"
    assert play._hosts == ['localhost'], "Hosts should be localhost"
    assert play._gather_facts is True, "Gather facts should be True"
    assert play._roles == ['webserver', 'database'], "Roles should include webserver and database"

# Test edge case scenario with empty lists or None values
def test_edge_case():
    datastructure = {
        'hosts': [],
        'gather_facts': None,
        'roles': []
    }
    play = Play.load(datastructure)
    
    assert isinstance(play, Play), "Expected an instance of Play"
    assert play._hosts == [], "Hosts should be an empty list"
    assert play._gather_facts is None, "Gather facts should be None"
    assert play._roles == [], "Roles should be an empty list"

# Test invalid input scenario
def test_invalid_input():
    datastructure = {
        'hosts': ['localhost'],
        'gather_facts': True,
        'roles': ['webserver', 'database'],
        'invalid_key': 'invalid_value'  # Invalid key to simulate invalid input
    }
    
    with pytest.raises(TypeError):
        Play.load(datastructure)
