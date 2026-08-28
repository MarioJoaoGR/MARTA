
import pytest
from ansible.playbook.play import Play

# Test Scenario 1: Valid Input
def test_valid_input():
    data = {'hosts': ['localhost'], 'gather_facts': True, 'roles': ['webserver', 'database']}
    play = Play.load(data)
    
    assert isinstance(play, Play)
    assert play._hosts == ['localhost']
    assert play._gather_facts is True
    assert play._roles == ['webserver', 'database']

# Test Scenario 2: Edge Case with Empty Hosts List
def test_edge_case():
    data = {'hosts': [], 'gather_facts': False, 'roles': []}
    play = Play.load(data)
    
    assert isinstance(play, Play)
    assert play._hosts == []
    assert play._gather_facts is False
    assert play._roles == []

# Test Scenario 3: Invalid Input Raising TypeError
def test_invalid_input():
    with pytest.raises(TypeError):
        Play.load(None)
