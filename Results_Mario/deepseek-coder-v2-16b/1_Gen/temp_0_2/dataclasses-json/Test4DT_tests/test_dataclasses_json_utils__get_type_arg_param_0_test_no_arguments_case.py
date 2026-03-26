
import pytest
from typing import Tuple, Type, Union, cast
from dataclasses_json.utils import _NO_ARGS, _get_type_arg_param

# Mocking the private function _get_type_args to return a fixed value for testing
def mock_get_type_args(tp: Type) -> Tuple[Type, ...]:
    if tp == Tuple:
        return (int, str)  # Example tuple with two types
    else:
        raise NotImplementedError("Unknown type")

# Monkey-patching the private function for testing
def _get_type_args(tp: Type) -> Tuple[Type, ...]:
    return mock_get_type_args(tp)

@pytest.mark.parametrize("input_type, index, expected", [
    (Tuple[int, str], 1, str),
    (Tuple[int, str], 0, int),
    (Tuple, 0, _NO_ARGS),
    (Tuple[int], 0, int),
    (Tuple[int, str], 2, _NO_ARGS)  # Index out of range
])
def test_get_type_arg_param(input_type, index, expected):
    result = _get_type_arg_param(input_type, index)
    assert result == expected
