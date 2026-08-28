
import pytest
from ansible.playbook.play import Play

# Test for valid input get_vars
def test_valid_input_get_vars():
    play = Play()
    play._vars = {'key1': 'value1', 'key2': 'value2'}
    assert play.get_vars() == {'key1': 'value1', 'key2': 'value2'}

# Test for edge case with an empty instance
def test_edge_case_empty_instance():
    play = Play()
    assert play.get_vars() == {}

# Test for invalid input get_vars (e.g., None)
def test_invalid_input_get_vars():
    play = Play()
    with pytest.raises(AttributeError):
        play.get_vars(None)
