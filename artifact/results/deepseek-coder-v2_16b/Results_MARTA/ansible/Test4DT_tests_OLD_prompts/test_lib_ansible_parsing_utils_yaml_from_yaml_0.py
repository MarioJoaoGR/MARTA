
import pytest
from ansible.parsing.utils.yaml import from_yaml
from ansible.errors import AnsibleParserError
from json import JSONDecodeError
from yaml import YAMLError



def test_valid_yaml():
    data = "key: value"
    parsed_data = from_yaml(data)
    assert isinstance(parsed_data, dict)
