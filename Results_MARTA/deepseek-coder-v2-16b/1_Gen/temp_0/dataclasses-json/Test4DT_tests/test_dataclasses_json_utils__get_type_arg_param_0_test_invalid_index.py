
import pytest
from typing import Tuple, Union, Type, cast
from dataclasses_json.utils import _get_type_arg_param, _NO_ARGS

def test_invalid_index():
    # Test with a valid generic type and an out-of-range index
    result = _get_type_arg_param(Tuple[int, str], 2)
    assert result == _NO_ARGS
