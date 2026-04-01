
import pytest
from io import BytesIO
from isort._vendored.tomli._parser import load as toml_load
from typing import Dict, Any

def test_valid_input_binary_mode():
    # Create a sample TOML content
    toml_content = b"""name = "John Doe"
age = 30
email = "john.doe@example.com"
"""
    
    # Open the BytesIO object in binary mode with the sample TOML content
    fp = BytesIO(toml_content)
    
    # Call the load function with the BytesIO object
    result = toml_load(fp)
    
    # Assert that the result is a dictionary and contains expected keys
    assert isinstance(result, dict), "Expected a dictionary but got something else"
    assert 'name' in result, "'name' key not found in the result"
    assert 'age' in result, "'age' key not found in the result"
    assert 'email' in result, "'email' key not found in the result"
    assert result['name'] == "John Doe", "Unexpected value for 'name'"
    assert result['age'] == 30, "Unexpected value for 'age'"
    assert result['email'] == "john.doe@example.com", "Unexpected value for 'email'"
