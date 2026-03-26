
import pytest
from isort._vendored.tomli._parser import load, ParseFloat
from io import StringIO
from tomllib import loads
import warnings

def test_valid_input():
    # Create a mock file-like object with valid TOML content
    toml_content = """key = "value"
float_val = 3.14
bool_val = true
int_val = 42"""
    fp = StringIO(toml_content)
    
    # Call the load function
    parsed_data = load(fp)
    
    # Check if the output is as expected
    assert parsed_data == {
        'key': 'value',
        'float_val': 3.14,
        'bool_val': True,
        'int_val': 42
    }

def test_valid_input_with_custom_parse_float():
    # Create a mock file-like object with valid TOML content
    toml_content = """key = "value"
float_val = 3.14"""
    fp = StringIO(toml_content)
    
    # Define a custom parse float function
    def custom_parse_float(s):
        return float(s) * 2  # Example of custom parsing
    
    # Call the load function with the custom parse float
    parsed_data = load(fp, parse_float=custom_parse_float)
    
    # Check if the output is as expected after applying custom parsing
    assert parsed_data == {
        'key': 'value',
        'float_val': 3.14 * 2  # Expected value after custom parsing
    }

def test_valid_input_with_deprecation():
    # Create a mock file-like object with valid TOML content
    toml_content = """key = "value"
float_val = 3.14"""
    fp = StringIO(toml_content)
    
    # Call the load function and suppress warnings
    with pytest.warns(DeprecationWarning):
        parsed_data = load(fp)
    
    # Check if the output is as expected, ignoring the deprecation warning
    assert parsed_data == {
        'key': 'value',
        'float_val': 3.14
    }
