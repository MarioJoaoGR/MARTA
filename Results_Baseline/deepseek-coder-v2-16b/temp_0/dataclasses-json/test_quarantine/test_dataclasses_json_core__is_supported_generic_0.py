
# Module: dataclasses_json.core
import pytest
from typing import List, Optional, Union, Enum
import enum
from dataclasses import dataclass  # Corrected import statement for dataclasses

# Define a hypothetical generic dataclass for demonstration purposes
@dataclass
class MyGenericDataclass:
    pass

# Mock helper functions to simulate the behavior of _issubclass_safe, _is_collection, _is_optional, is_union_type, and _is_generic_dataclass
def _issubclass_safe(cls, base):
    return issubclass(cls, base)

def _is_collection(typ):
    from collections.abc import Collection
    return isinstance(typ, Collection)

def _is_optional(typ):
    from typing import Optional
    return isinstance(typ, Optional) or typ == type(None)

def is_union_type(typ):
    from types import UnionType
    return isinstance(typ, UnionType)

def _is_generic_dataclass(typ):
    return hasattr(typ, '__origin__') and typ.__origin__ == dataclass  # Corrected the reference to dataclass

# Import the function with its module name
from dataclasses_json.core import _is_supported_generic

# Test cases for _is_supported_generic
def test_is_supported_generic_list():
    assert _is_supported_generic(List[int]) == True, "Expected List[int] to be supported"

def test_is_supported_generic_optional():
    assert _is_supported_generic(Optional[int]) == True, "Expected Optional[int] to be supported"

def test_is_supported_generic_enum():
    class MyEnum(enum.Enum):
        A = 1
    assert _is_supported_generic(MyEnum) == False, "Expected MyEnum not to be supported as it is an enum"

def test_is_supported_generic_generic_dataclass():
    assert _is_supported_generic(MyGenericDataclass) == False, "Expected MyGenericDataclass not to be supported as it is a generic dataclass"

def test_is_supported_generic_str():
    assert _is_supported_generic(str) == False, "Expected str not to be supported"

def test_is_supported_generic_int():
    assert _is_supported_generic(int) == True, "Expected int to be supported"

# Run the tests with pytest
if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__is_supported_generic_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0.py:4:0: E0611: No name 'Enum' in module 'typing' (no-name-in-module)

"""