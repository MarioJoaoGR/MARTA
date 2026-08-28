
# Module: ansible.playbook.play
# test_play.py
from ansible.playbook import Play
import pytest
from ansible.errors import AnsibleParserError

@pytest.fixture
def play():
    return Play()

def test_load_vars_prompt_empty_input(play):
    result = play._load_vars_prompt('attr_name', None)
    assert isinstance(result, list), "Expected a list of dictionaries"
    assert len(result) == 0, "Expected an empty list for no input data"

def test_load_vars_prompt_invalid_structure(play):
    invalid_data = [{'name': 'example_name', 'prompt': 'Example prompt', 'default': 'default_value', 'unsupported': 'value'}]
    with pytest.raises(AnsibleParserError) as excinfo:
        play._load_vars_prompt('attr_name', invalid_data)
    assert "found unsupported key 'unsupported'" in str(excinfo.value), "Expected error message about unsupported key"

def test_load_vars_prompt_missing_name_key(play):
    invalid_data = [{'prompt': 'Example prompt', 'default': 'default_value'}]
    with pytest.raises(AnsibleParserError) as excinfo:
        play._load_vars_prompt('attr_name', invalid_data)
    assert "missing 'name' key" in str(excinfo.value), "Expected error message about missing 'name' key"

def test_load_vars_prompt_valid_structure(play):
    valid_data = [{'name': 'example_name', 'prompt': 'Example prompt', 'default': 'default_value'}]
    result = play._load_vars_prompt('attr_name', valid_data)
    assert isinstance(result, list), "Expected a list of dictionaries"
    assert len(result) == 1, "Expected one entry in the list"
    assert 'name' in result[0], "'name' key is missing"
    assert result[0]['name'] == 'example_name', "'name' does not match expected value"

def test_load_vars_prompt_valid_structure_with_extra_keys(play):
    valid_data = [{'name': 'example_name', 'prompt': 'Example prompt', 'default': 'default_value', 'private': True, 'confirm': False}]
    result = play._load_vars_prompt('attr_name', valid_data)
    assert isinstance(result, list), "Expected a list of dictionaries"
    assert len(result) == 1, "Expected one entry in the list"
    assert 'name' in result[0], "'name' key is missing"
    assert result[0]['name'] == 'example_name', "'name' does not match expected value"
    assert 'private' in result[0], "'private' key is missing"
    assert result[0]['private'] is True, "'private' does not match expected value"
    assert 'confirm' in result[0], "'confirm' key is missing"
    assert result[0]['confirm'] is False, "'confirm' does not match expected value"
