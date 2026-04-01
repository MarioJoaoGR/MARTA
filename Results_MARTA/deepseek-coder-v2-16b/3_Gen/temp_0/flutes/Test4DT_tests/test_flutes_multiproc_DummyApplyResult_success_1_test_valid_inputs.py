
import pytest
from unittest.mock import patch
from flutes.multiproc import DummyApplyResult

def test_valid_inputs():
    # Test with an integer value
    result = DummyApplyResult(42)
    assert result._value == 42
    
    # Test with a string value
    result_str = DummyApplyResult("Hello, World!")
    assert result_str._value == "Hello, World!"
    
    # Test with a float value
    result_float = DummyApplyResult(3.14)
    assert result_float._value == 3.14
    
    # Test with a list value
    result_list = DummyApplyResult([1, 2, 3])
    assert result_list._value == [1, 2, 3]
    
    # Test with a dictionary value
    result_dict = DummyApplyResult({"key": "value"})
    assert result_dict._value == {"key": "value"}
