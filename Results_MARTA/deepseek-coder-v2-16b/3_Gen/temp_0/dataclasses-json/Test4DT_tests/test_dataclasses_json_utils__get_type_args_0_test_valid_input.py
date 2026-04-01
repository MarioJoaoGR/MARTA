
import pytest
from typing import Tuple, Type, Union
from dataclasses_json.utils import _get_type_args, _NO_ARGS

def test_valid_input():
    # Test with a valid generic type
    result = _get_type_args(Tuple[int, str])
    assert result == (int, str)
    
    # Test without default value provided
    result_no_default = _get_type_args(Tuple[int, str], _NO_ARGS)
    assert result_no_default == (int, str)
    
    # Test with a specific default value
    def some_function():
        return _get_type_args(Tuple[int, str], (str,))
    result_with_default = some_function()
    assert result_with_default == (int, str)
