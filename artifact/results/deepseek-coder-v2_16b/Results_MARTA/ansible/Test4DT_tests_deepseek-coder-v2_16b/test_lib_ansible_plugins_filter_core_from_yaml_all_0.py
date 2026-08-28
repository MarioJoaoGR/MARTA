
import pytest
from ansible.plugins.filter import core
from io import StringIO
import yaml

# Mocking the necessary functions for testing
class MockSafeLoader(yaml.SafeLoader):
    pass

def mock_yaml_load_all(data):
    return list(yaml.load_all(data, Loader=MockSafeLoader))

core.yaml_load_all = mock_yaml_load_all

# Test cases
@pytest.mark.parametrize("input_data", [('key: value',), (None,)])
def test_valid_yaml_string(input_data):
    data, expected_output = input_data
    result = core.from_yaml_all(data)
    if data is None:
        assert result == data
    else:
        assert result == [{'key': 'value'}]

@pytest.mark.parametrize("input_data", [('key: value',), (None,)])
def test_invalid_yaml_string(input_data):
    data, expected_output = input_data
    with pytest.raises(yaml.YAMLError):
        core.from_yaml_all(data)
