# Module: ansible.playbook.play
# test_play.py
from ansible.playbook import Play
import pytest

@pytest.fixture
def play():
    return Play()

def test_load_vars_prompt_valid(play):
    valid_data = [{'name': 'example_name', 'prompt': 'Example prompt', 'default': 'default_value'}]
    result = play._load_vars_prompt('attr_name', valid_data)
    assert isinstance(result, list), "Expected a list of dictionaries"
    assert len(result) == 1, "Expected one entry in the list"
    assert 'name' in result[0], "'name' key is missing"
    assert result[0]['name'] == 'example_name', "'name' does not match expected value"

def test_load_vars_prompt_invalid_missing_name(play):
    invalid_data = [{'prompt': 'Example prompt', 'default': 'default_value'}]
    with pytest.raises(AnsibleParserError) as excinfo:
        play._load_vars_prompt('attr_name', invalid_data)
    assert "missing 'name' key" in str(excinfo.value), "Expected error message about missing 'name' key"

def test_load_vars_prompt_invalid_unsupported_key(play):
    invalid_data = [{'name': 'example_name', 'prompt': 'Example prompt', 'default': 'default_value', 'unsupported': 'value'}]
    with pytest.raises(AnsibleParserError) as excinfo:
        play._load_vars_prompt('attr_name', invalid_data)
    assert "found unsupported key 'unsupported'" in str(excinfo.value), "Expected error message about unsupported key"
