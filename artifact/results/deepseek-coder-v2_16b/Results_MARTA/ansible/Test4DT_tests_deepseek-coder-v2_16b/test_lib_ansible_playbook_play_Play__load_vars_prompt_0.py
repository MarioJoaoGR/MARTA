
import pytest
from ansible.playbook.play import Play
from ansible.errors import AnsibleParserError

# Test valid input scenario
def test_valid_input():
    datastructure = {
        'hosts': ['localhost'],
        'roles': ['role1', 'role2']
    }
    play = Play.load(datastructure)
    
    assert isinstance(play, Play)
    assert play._hosts == ['localhost']
    assert play._gather_facts is None
    assert play._roles == ['role1', 'role2']

# Test edge case scenario with invalid input data structures
@pytest.mark.parametrize("datastructure", [None, {}, {'hosts': []}, {'roles': []}])
def test_edge_case(datastructure):
    with pytest.raises(AnsibleParserError):
        Play.load(datastructure)

# Test handling of invalid inputs by raising AnsibleParserError
def test_invalid_input():
    datastructure = {
        'hosts': ['localhost'],
        'roles': ['role1', 'role2']
    }
    del datastructure['roles']
    
    with pytest.raises(AnsibleParserError):
        Play.load(datastructure)
