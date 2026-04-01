
import pytest
from isort._vendored.tomli._parser import load, ParseFloat
from io import StringIO
from tomllib import loads
import warnings

def test_valid_input():
    # Create a mock file-like object with TOML content
    toml_content = """key1 = "value1"
key2 = 3.14
list_key = [1, 2, 3]"""
    fp = StringIO(toml_content)
    
    # Call the load function
    result = load(fp)
    
    # Check if the result is a dictionary and has the expected keys and values
    assert isinstance(result, dict)
    assert result == {'key1': 'value1', 'key2': 3.14, 'list_key': [1, 2, 3]}
    
    # Check if deprecation warning is raised when reading from text mode file object
    with pytest.warns(DeprecationWarning):
        fp = StringIO("")
        load(fp)
