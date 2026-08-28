
import pytest
from ansible.plugins.filter.core import to_nice_yaml
import yaml

def test_to_nice_yaml_basic():
    # Test basic functionality of to_nice_yaml with a simple dictionary
    input_data = {'key': 'value'}
    expected_output = '''key: value
'''
    
    result = to_nice_yaml(input_data)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

# Add more tests if needed
