
# Module: ansible.playbook.play
# test_play.py
from ansible.playbook import Play
import pytest
from ansible.errors import AnsibleParserError

@pytest.fixture
def play():
    return Play()

# Test case for valid vars_prompt data structure
def test_load_vars_prompt_valid(play):
    valid_data = [{'name': 'example_name', 'prompt': 'Example prompt', 'default': 'default_value'}]
    result = play._load_vars_prompt('attr_name', valid_data)
    assert isinstance(result, list), "Expected a list of dictionaries"
    assert len(result) == 1, "Expected one entry in the list"
    assert 'name' in result[0], "'name' key is missing"
    assert result[0]['name'] == 'example_name', "'name' does not match expected value"

# Test case for invalid vars_prompt data structure with missing 'name' key
def test_load_vars_prompt_invalid_missing_name(play):
    invalid_data = [{'prompt': 'Example prompt', 'default': 'default_value'}]
    with pytest.raises(AnsibleParserError) as excinfo:
        play._load_vars_prompt('attr_name', invalid_data)
    assert "missing 'name' key" in str(excinfo.value), "Expected error message about missing 'name' key"

# Test case for invalid vars_prompt data structure with unsupported key
def test_load_vars_prompt_invalid_unsupported_key(play):
    invalid_data = [{'name': 'example_name', 'prompt': 'Example prompt', 'default': 'default_value', 'unsupported': 'value'}]
    with pytest.raises(AnsibleParserError) as excinfo:
        play._load_vars_prompt('attr_name', invalid_data)
    assert "found unsupported key 'unsupported'" in str(excinfo.value), "Expected error message about unsupported key"

# Test case for empty vars_prompt data structure
def test_load_vars_prompt_empty(play):
    result = play._load_vars_prompt('attr_name', [])
    assert isinstance(result, list), "Expected an empty list for no input"
    assert len(result) == 0, "Expected zero entries in the list for no input"

# Test case for vars_prompt data structure with only mandatory keys but no 'default' value
def test_load_vars_prompt_mandatory_keys_only(play):
    mandatory_data = [{'name': 'example_name', 'prompt': 'Example prompt'}]
    result = play._load_vars_prompt('attr_name', mandatory_data)
    assert isinstance(result, list), "Expected a list of dictionaries"
    assert len(result) == 1, "Expected one entry in the list"
    assert 'name' in result[0], "'name' key is missing"
    assert result[0]['name'] == 'example_name', "'name' does not match expected value"