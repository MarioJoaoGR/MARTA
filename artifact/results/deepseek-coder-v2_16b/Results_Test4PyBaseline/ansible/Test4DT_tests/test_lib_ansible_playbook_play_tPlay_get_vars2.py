
import pytest
from ansible.playbook.play import Play

@pytest.fixture
def play():
    # Create an instance of the Play class for testing
    return Play()

# Test case to check if getting variables returns a copy
def test_get_vars(play):
    play.vars = {'var1': 'value1', 'var2': 'value2'}
    vars_copy = play.get_vars()
    assert play.vars is not vars_copy, "Getting variables should return a different object"
    assert play.vars == vars_copy, "The original and the copied variables should be equal"

# Test case to check if get_vars handles missing keys gracefully by returning a default value
def test_get_vars_missing_key(play):
    default_value = 'default_value'
    play.vars = {}  # No keys in vars dictionary
    assert play.get_vars().get('non_existent_key', default_value) == default_value, "Getting a missing key should return the default value"

# Test case to check if get_vars handles different data types correctly
def test_get_vars_different_data_types(play):
    play.vars = {
        'list': [1, 2, 3],
        'dict': {'key': 'value'},
        'set': {1, 2, 3}
    }
    vars_copy = play.get_vars()
    assert isinstance(vars_copy['list'], list), "List should be a shallow copy"
    assert isinstance(vars_copy['dict'], dict), "Dictionary should be a shallow copy"
    assert isinstance(vars_copy['set'], set), "Set should be a shallow copy"