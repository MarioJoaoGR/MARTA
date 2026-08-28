
import pytest
from ansible.playbook.play import Play
from unittest.mock import patch

# Test for valid inputs - happy path
def test_valid_inputs_happy_path():
    play = Play()
    play.load({
        'hosts': ['localhost'],
        'gather_facts': True,
        'roles': ['webserver', 'database']
    })
    
    assert play._hosts == ['localhost']
    assert play._gather_facts is True
    assert play._roles == ['webserver', 'database']

# Test for edge cases
def test_edge_cases():
    play = Play()
    play.load({})  # Empty dictionary
    
    assert not hasattr(play, '_hosts')  # No hosts should be set
    assert not hasattr(play, '_gather_facts')  # gather_facts should not be set
    assert not hasattr(play, '_roles')  # roles should not be set

# Test for invalid inputs - error handling
def test_invalid_inputs_error_handling():
    with pytest.raises(ValueError):
        play = Play()
        play.load({'hosts': None})  # Invalid hosts input
