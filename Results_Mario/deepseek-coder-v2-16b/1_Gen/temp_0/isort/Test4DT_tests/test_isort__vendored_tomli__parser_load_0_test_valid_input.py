
from isort._vendored.tomli._parser import load, ParseFloat, Dict, IO, loads, warnings
import pytest

def test_valid_input():
    # Create a mock file object with valid TOML content
    from io import StringIO
    tom_content = """name = "Tom"
age = 42"""
    fp = StringIO(tom_content)
    
    # Call the load function
    parsed_data = load(fp)
    
    # Assert that the parsed data is a dictionary
    assert isinstance(parsed_data, dict)
    
    # Assert specific keys and values in the parsed data
    assert "name" in parsed_data
    assert parsed_data["name"] == "Tom"
    assert "age" in parsed_data
    assert parsed_data["age"] == 42
