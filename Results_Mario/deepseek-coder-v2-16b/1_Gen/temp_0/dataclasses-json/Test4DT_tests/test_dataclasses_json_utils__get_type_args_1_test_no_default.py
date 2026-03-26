
import pytest
from typing import Tuple, Type, Union
from dataclasses_json.utils import _get_type_args, _NO_ARGS

def test_no_default():
    # Test when no default is provided
    tp = Tuple[int, str]
    result = _get_type_args(tp)
    assert result == (int, str)
