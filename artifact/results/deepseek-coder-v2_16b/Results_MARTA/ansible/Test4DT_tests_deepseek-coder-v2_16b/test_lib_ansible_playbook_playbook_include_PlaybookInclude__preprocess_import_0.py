
import pytest
from ansible.playbook import PlaybookInclude
from ansible.errors import AnsibleParserError

# Test cases for PlaybookInclude class
def test_valid_input_happy_path():
    data = {'import_playbook': 'example_playbook.yml', 'vars': {'key1': 'value1', 'key2': 'value2'}}
    include = PlaybookInclude()
    with pytest.raises(AnsibleParserError):
        include._preprocess_import(None, data, 'import_playbook', None)
    assert data['import_playbook'] == 'example_playbook.yml'
    assert data['vars'] == {'key1': 'value1', 'key2': 'value2'}

def test_missing_parameter():
    data = {'import_playbook': None}
    include = PlaybookInclude()
    with pytest.raises(AnsibleParserError) as excinfo:
        include._preprocess_import(None, data, 'import_playbook', None)
    assert str(excinfo.value) == "playbook import parameter is missing"

def test_invalid_type_parameter():
    data = {'import_playbook': 12345}
    include = PlaybookInclude()
    with pytest.raises(AnsibleParserError) as excinfo:
        include._preprocess_import(None, data, 'import_playbook', 12345)
    assert str(excinfo.value) == "playbook import parameter must be a string indicating a file path, got <class 'int'> instead"
