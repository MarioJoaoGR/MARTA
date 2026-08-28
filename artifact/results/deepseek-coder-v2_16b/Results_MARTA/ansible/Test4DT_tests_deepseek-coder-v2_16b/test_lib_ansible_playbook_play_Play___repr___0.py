
import pytest
from ansible.playbook.play import Play

# Test for valid case scenario
def test_valid_case():
    play_config = {
        'hosts': ['localhost'],
        'roles': ['role1', 'role2']
    }
    play = Play.load(play_config)
    
    assert isinstance(play, Play), "Expected an instance of Play"
    assert play._hosts == ['localhost'], "Hosts should be localhost"
    assert play._roles == ['role1', 'role2'], "Roles should include role1 and role2"
    assert not play.skip_tags, "Skip tags should be empty by default"
    assert not play.only_tags, "Only tags should be empty by default"
    assert not play.force_handlers, "Force handlers should be False by default"

# Test for edge case scenario with None values
def test_edge_case():
    play = Play()
    
    assert isinstance(play, Play), "Expected an instance of Play"
    assert not play._hosts, "Hosts list should be empty"
    assert play._gather_facts is None, "Gather facts should be None by default"
    assert play._roles == [], "Roles list should be empty"
    assert not play.skip_tags, "Skip tags should be empty by default"
    assert not play.only_tags, "Only tags should be empty by default"
    assert not play.force_handlers, "Force handlers should be False by default"

# Test for invalid input scenario with invalid configuration
def test_invalid_input():
    play_config = {
        'hosts': ['localhost'],
        'roles': [],  # Invalid: empty roles list
        'invalid_key': 'value'  # Invalid: additional key with value
    }
    
    with pytest.raises(ValueError):
        Play.load(play_config)
