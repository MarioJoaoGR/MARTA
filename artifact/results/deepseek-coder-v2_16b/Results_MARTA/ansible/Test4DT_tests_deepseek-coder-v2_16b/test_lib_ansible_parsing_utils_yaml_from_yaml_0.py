
import pytest
from ansible.parsing.utils.yaml import from_yaml
from ansible.errors import AnsibleParserError
import json


def test_invalid_json():
    invalid_json = "invalid: json"
    with pytest.raises(AnsibleParserError):
        from_yaml(invalid_json, json_only=True)

def test_valid_yaml():
    valid_yaml = """
    key: value
    """
    parsed_data = from_yaml(valid_yaml)
    assert isinstance(parsed_data, dict)
    assert parsed_data['key'] == 'value'
