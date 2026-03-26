
import pytest
from typing import Tuple, Type, Union
from dataclasses_json.utils import _NO_ARGS, _get_type_args

def test_valid_input_with_generic_type():
    # Test with a valid generic type (Tuple[int, str]) and no default value provided
    result = _get_type_args(Tuple[int, str])
    assert result == (int, str)
