
import pytest
from typing import Tuple, Type, Union, cast
from dataclasses_json.utils import _get_type_arg_param, _NO_ARGS

def test_valid_input():
    # Test with a generic type having multiple arguments
    result = _get_type_arg_param(Tuple[int, str], 1)
    assert isinstance(result, type) and result == str
    
    # Test with a generic type having only one argument
    result = _get_type_arg_param(Tuple[int, ...], 0)
    assert isinstance(result, type) and result == int
    
    # Test where the index is out of range
    result = _get_type_arg_param(Tuple[int, str], 2)
    assert result == _NO_ARGS
