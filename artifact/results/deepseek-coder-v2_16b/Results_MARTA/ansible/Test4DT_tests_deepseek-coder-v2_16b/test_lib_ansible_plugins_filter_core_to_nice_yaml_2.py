
import pytest
from ansible.plugins.filter.core import to_nice_yaml
import yaml

# Test for basic functionality of to_nice_yaml function
def test_to_nice_yaml_basic():
    # Define a simple dictionary to be converted to YAML
    data = {'key': 'value'}
    
    # Call the function with the defined data and default indent
    result = to_nice_yaml(data)
    
    # Load the result into PyYAML to check if it's in nice YAML format
    parsed_result = yaml.safe_load(result)
    
    # Assert that the parsed result is a dictionary and contains the expected key-value pair
    assert isinstance(parsed_result, dict)
    assert parsed_result['key'] == 'value'

# Test for custom indentation in to_nice_yaml function
def test_to_nice_yaml_custom_indent():
    # Define a simple dictionary to be converted to YAML
    data = {'key': 'value'}
    
    # Call the function with the defined data and custom indent of 2 spaces
    result = to_nice_yaml(data, indent=2)
    
    # Load the result into PyYAML to check if it's in nice YAML format with custom indentation
    parsed_result = yaml.safe_load(result)
    
    # Assert that the parsed result is a dictionary and contains the expected key-value pair
    assert isinstance(parsed_result, dict)
    assert parsed_result['key'] == 'value'
    # Check if the indentation matches the custom indent setting
    assert len(result.split('\n')) > 1 and all([line.startswith(' ') for line in result.split('\n')])

# Test for additional keyword arguments in to_nice_yaml function
def test_to_nice_yaml_additional_kwargs():
    # Define a simple dictionary to be converted to YAML
    data = {'key': 'value'}
    
    # Call the function with the defined data and additional keyword argument allow_unicode=True
    result = to_nice_yaml(data, indent=2, allow_unicode=True)
    
    # Load the result into PyYAML to check if it's in nice YAML format with custom indentation and allow_unicode setting
    parsed_result = yaml.safe_load(result)
    
    # Assert that the parsed result is a dictionary and contains the expected key-value pair
    assert isinstance(parsed_result, dict)
    assert parsed_result['key'] == 'value'
    # Check if the indentation matches the custom indent setting and allow_unicode is True
    assert len(result.split('\n')) > 1 and all([line.startswith(' ') for line in result.split('\n')])
    assert "unicode" in result
