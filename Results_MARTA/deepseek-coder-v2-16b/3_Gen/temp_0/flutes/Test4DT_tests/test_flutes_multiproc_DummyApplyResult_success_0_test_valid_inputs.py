
import pytest
from unittest.mock import patch
from flutes.multiproc import DummyApplyResult

def test_valid_inputs():
    # Test with integer value
    result_int = DummyApplyResult(42)
    assert result_int.success() is True
    
    # Test with string value
    result_str = DummyApplyResult("Success")
    assert result_str.success() is True
    
    # Test with float value
    result_float = DummyApplyResult(3.14)
    assert result_float.success() is True
    
    # Test with list value
    result_list = DummyApplyResult([1, 2, 3])
    assert result_list.success() is True
    
    # Test with dictionary value
    result_dict = DummyApplyResult({"key": "value"})
    assert result_dict.success() is True
    
    # Test with None value
    result_none = DummyApplyResult(None)
    assert result_none.success() is True
