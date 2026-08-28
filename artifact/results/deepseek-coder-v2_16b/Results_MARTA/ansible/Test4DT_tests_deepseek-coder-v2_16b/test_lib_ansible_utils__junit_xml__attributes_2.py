
import pytest
from ansible.utils._junit_xml import _attributes
import typing as t

def test_valid_inputs():
    # Test valid inputs to check correct behavior
    result = _attributes(a=123, b="test", c=None)
    assert isinstance(result, dict), "Expected a dictionary"
    assert len(result) == 2, "Expected two key-value pairs"
    assert result['a'] == '123', "Expected value for 'a' to be '123'"
    assert result['b'] == 'test', "Expected value for 'b' to be 'test'"

def test_none_values():
    # Test inputs with None values to ensure they are omitted
    result = _attributes(x=True, y=False, z=None)
    assert isinstance(result, dict), "Expected a dictionary"
    assert len(result) == 2, "Expected two key-value pairs"
    assert 'z' not in result, "Expected None value to be omitted"

def test_no_arguments():
    # Test function with no arguments provided
    result = _attributes()
    assert isinstance(result, dict), "Expected a dictionary"
    assert len(result) == 0, "Expected an empty dictionary for no arguments"
