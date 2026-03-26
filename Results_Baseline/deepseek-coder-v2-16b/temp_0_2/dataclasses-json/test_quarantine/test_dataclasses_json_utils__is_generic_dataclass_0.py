
# Module: dataclasses_json.utils
import pytest
from typing import List, Union
from dataclasses import is_dataclass
from inspect import getmodule, _get_type_origin
from dataclasses_json.utils import _is_generic_dataclass

# Test cases for _is_generic_dataclass function
def test_is_generic_dataclass_with_list():
    my_list = [1, 2, 3]
    type_of_my_list = type(my_list)
    assert _is_generic_dataclass(type_of_my_list), "Expected True for a list which is a generic dataclass"

def test_is_generic_dataclass_with_union():
    mixed_types = Union[int, str]
    type_of_mixed_types = type(mixed_types)
    assert not _is_generic_dataclass(type_of_mixed_types), "Expected False for a union which is not a dataclass"

def test_is_generic_dataclass_with_custom_generic():
    from typing import Generic, TypeVar
    T = TypeVar('T')
    class CustomGeneric(Generic[T]):
        pass
    custom_instance = CustomGeneric[int]()
    type_of_custom_instance = type(custom_instance)
    assert _is_generic_dataclass(type_of_custom_instance), "Expected True for a custom generic class"

def test_is_generic_dataclass_with_non_generic():
    class NonGenericClass:
        pass
    non_generic_instance = NonGenericClass()
    type_of_non_generic_instance = type(non_generic_instance)
    assert not _is_generic_dataclass(type_of_non_generic_instance), "Expected False for a non-generic class"

def test_is_generic_dataclass_with_none():
    with pytest.raises(TypeError):
        assert not _is_generic_dataclass(None), "Expected TypeError when passing None"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__is_generic_dataclass_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_generic_dataclass_0.py:6:0: E0611: No name '_get_type_origin' in module 'inspect' (no-name-in-module)

"""