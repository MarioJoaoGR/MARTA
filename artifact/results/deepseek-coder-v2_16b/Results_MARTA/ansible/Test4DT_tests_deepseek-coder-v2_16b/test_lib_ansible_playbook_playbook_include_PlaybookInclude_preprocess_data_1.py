
import pytest
from ansible.playbook.playbook_include import PlaybookInclude
from ansible.errors import AnsibleAssertionError, AnsibleParserError

# Test cases for PlaybookInclude.preprocess_data method

def test_valid_input():
    include = PlaybookInclude()
    ds = {'import_playbook': 'example_playbook.yml', 'tags': 'test', 'vars': {'param1': 'value1', 'param2': 'value2'}}
    result = include.preprocess_data(ds)
    assert isinstance(result, dict), "Expected a dictionary but got something else"
    assert 'import_playbook' in result, "'import_playbook' key is missing from the result"
    assert result['import_playbook'] == 'example_playbook.yml', "Incorrect import playbook filename"
    assert 'tags' in result, "'tags' key is missing from the result"
    assert result['tags'] == 'test', "Incorrect tags value"
    assert 'vars' in result, "'vars' key is missing from the result"
    assert isinstance(result['vars'], dict), "Expected a dictionary for 'vars'"
    assert result['vars']['param1'] == 'value1', "Incorrect value for param1"
    assert result['vars']['param2'] == 'value2', "Incorrect value for param2"

def test_none_input():
    include = PlaybookInclude()
    ds = None
    with pytest.raises(AnsibleAssertionError):
        include.preprocess_data(ds)

def test_invalid_input():
    include = PlaybookInclude()
    ds = {'import_playbook': 'example_playbook.yml', 'vars': {'param1': 'value1'}}
    with pytest.raises(AnsibleParserError):
        include.preprocess_data(ds)
