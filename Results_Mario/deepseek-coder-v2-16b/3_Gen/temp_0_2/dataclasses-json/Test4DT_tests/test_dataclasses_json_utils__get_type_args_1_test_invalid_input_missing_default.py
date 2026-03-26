
import pytest
from typing import Tuple, Type, Union
from dataclasses_json.utils import _get_type_args, _NO_ARGS

def test_invalid_input_missing_default():
    class MyType(Tuple[int, str]): pass
    
    # Create an instance of MyType with __args__ set to None
    my_type = MyType()
    my_type.__args__ = None
    
    result = _get_type_args(my_type)
    assert result == _NO_ARGS, f"Expected _NO_ARGS but got {result}"
