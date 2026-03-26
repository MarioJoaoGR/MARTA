
import pytest
from typing import Optional
import inspect
from dataclasses_json.utils import _is_optional, _is_new_type

# Test cases for _is_optional function
def test_is_optional_with_optional_hint():
    def my_function(arg: Optional[int] = None) -> None:
        pass
    result1 = _is_optional(my_function.__annotations__["arg"])
    assert result1 is True, "Expected True for an optional type hint"

def test_is_optional_with_non_optional_hint():
    def another_function(arg: int):
        pass
    result2 = _is_optional(another_function.__annotations__["arg"])
    assert result2 is False, "Expected False for a non-optional type hint"

def test_is_optional_with_custom_union_type():
    def custom_function(arg: Optional[int] = None):
        pass
    result3 = _is_optional(custom_function.__annotations__["arg"])
    assert result3 is True, "Expected True for an optional type hint with a custom union"

# Test cases for _is_new_type function
def test_is_new_type_with_new_type():
    class CustomType:
        def __supertype__(self):
            return int
    