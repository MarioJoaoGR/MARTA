
import pytest
from ansible.utils._junit_xml import _attributes
import typing as t

def test_valid_inputs():
    # Test with valid inputs (should not raise TypeError)
    result = _attributes(a=123, b="test", c=None)
    assert isinstance(result, dict), "Expected a dictionary"
    assert len(result) == 2, "Expected two key-value pairs"
    assert result['a'] == '123', "Expected value for key 'a' to be '123'"
    assert result['b'] == 'test', "Expected value for key 'b' to be 'test'"
