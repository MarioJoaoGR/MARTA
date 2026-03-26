
import pytest
from typing import Tuple, Union
from dataclasses_json.utils import _NO_ARGS, _get_type_args

# Test cases for _get_type_args function
def test_get_type_args_with_generic_type():
    from typing import Tuple
    tp = Tuple[int, str]
    result = _get_type_args(tp)
    assert result == (int, str)

def test_get_type_args_without_default():
    from typing import Tuple
    tp = Tuple[int, str]
    result = _get_type_args(tp)
    assert result == (int, str)

def test_get_type_args_with_specific_default():
    from typing import Tuple
    tp = Tuple[int, str]
    default = (str,)
    result = _get_type_args(tp, default)
    assert result == (int, str)

def test_get_type_args_with_none_args():
    from typing import List
    tp = List[int]
    result = _get_type_args(tp)