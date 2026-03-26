
import pytest
from typing import Tuple, Type, Union
from dataclasses_json.utils import _get_type_args, _NO_ARGS

def test_valid_input_without_args():
    # Test case where the type has no __args__ attribute and default is provided
    tp = Tuple[int, str]
    result = _get_type_args(tp)
    assert result == (int, str)
    
    # Test case where the type has no __args__ attribute and default is provided as an empty tuple
    tp = Tuple
    result = _get_type_args(tp, ())
    assert result == ()
    
    # Test case where the type has no __args__ attribute and default is provided as None
    tp = Tuple
    result = _get_type_args(tp, _NO_ARGS)
    assert result == _NO_ARGS
