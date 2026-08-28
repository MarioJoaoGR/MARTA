
import pytest
from ansible.plugins.filter.core import to_yaml
import yaml
from ansible.module_utils.common.json import AnsibleDumper
from ansible.module_utils.six import text_type, binary_type

def test_to_yaml_basic():
    # Define the dictionary to convert
    data = {'key': 'value'}
    
    # Call the function with the dictionary
    yaml_output = to_yaml(data)
    
    # Convert the YAML output back to a Python object
    parsed_data = yaml.safe_load(yaml_output)
    
    # Assert that the parsed data matches the original data
    assert parsed_data == data
