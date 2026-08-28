
import pytest
from ansible.parsing.utils.yaml import from_yaml
from ansible.errors import AnsibleParserError
import yaml
import json

# Test valid YAML input parsing
def test_valid_yaml_input():
    data = "key: value"
    parsed_data = from_yaml(data)
    assert isinstance(parsed_data, dict)
    assert parsed_data['key'] == 'value'

# Test handling None input gracefully
def test_none_input():
    with pytest.raises(AnsibleParserError):
        from_yaml(None)

# Test error handling for invalid JSON input
def test_invalid_json_error():
    data = "invalid json"
    with pytest.raises(AnsibleParserError):
        from_yaml(data, json_only=True)
