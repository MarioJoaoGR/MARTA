
import pytest
from typing import Tuple, Type, Union
from dataclasses_json.utils import _get_type_args, _NO_ARGS

def test_invalid_input():
    # Test with an invalid input (e.g., None)
    tp = None
    result = _get_type_args(tp)
    assert result == _NO_ARGS
