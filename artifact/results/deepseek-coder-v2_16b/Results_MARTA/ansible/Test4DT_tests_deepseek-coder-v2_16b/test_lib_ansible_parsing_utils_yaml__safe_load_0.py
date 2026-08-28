
import pytest
from ansible.parsing.utils.yaml import _safe_load
import yaml
import os

# Fixtures for common setup and teardown tasks
@pytest.fixture(scope="module")
def valid_yaml_string():
    return """
    key: value
    list:
        - item1
        - item2
    """

@pytest.fixture(scope="module")
def valid_yaml_file(tmpdir_factory):
    content = """
    key: value
    list:
        - item1
        - item2
    """
    file_path = tmpdir_factory.mktemp("data").join("valid.yml")
    with open(file_path, 'w') as f:
        f.write(content)
    return file_path

@pytest.fixture(scope="module")
def invalid_input():
    return None

# Test scenarios
def test_valid_input_string(valid_yaml_string):
    loaded_data = _safe_load(valid_yaml_string)
    assert isinstance(loaded_data, dict)
    assert loaded_data['key'] == 'value'
    assert loaded_data['list'] == ['item1', 'item2']

def test_valid_input_file(valid_yaml_file):
    with open(valid_yaml_file, 'r') as f:
        loaded_data = _safe_load(f)
    assert isinstance(loaded_data, dict)
    assert loaded_data['key'] == 'value'
    assert loaded_data['list'] == ['item1', 'item2']

def test_invalid_input_error_handling(invalid_input):
    with pytest.raises(TypeError):
        _safe_load(invalid_input)
