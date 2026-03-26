
# Module: dataclasses_json.mm
import pytest
from dataclasses import dataclass, fields
from typing import Optional, List, Tuple, Union, Dict, Any, Callable
from enum import Enum
from marshmallow import Schema, fields as mfields
from warnings import warn

# Mocking the necessary functions and constants for testing
def _is_new_type(type_: type) -> bool: return False
def _issubclass_safe(cls: type, mixin: type) -> bool: return False
def is_dataclass(cls: type) -> bool: return False
def _is_supported_generic(typ: type) -> bool: return False
def _is_collection(typ: type) -> bool: return False
def _is_optional(typ: type) -> bool: return False
def is_union_type(typ: type) -> bool: return False
def TYPES(): return {}
def _TupleVarLen(item_type, **options): return mfields.List(item_type, **options)
def _UnionField(union_desc, cls, field, **options): return mfields.Raw(**options)

# Mocking the module and its functions for testing
class Undefined:
    EXCLUDE = None

@dataclass
class Person:
    name: str
    age: int
    city: Optional[str] = None

@pytest.fixture
def person():
    return Person(name="John Doe", age=30, city=Undefined.EXCLUDE)

# Test cases for build_type function
def test_build_type_with_dataclass():
    @dataclass
    class Address:
        street: str
        number: int

    field = mfields.Field(name="address", type=Address)
    result = build_type(Address, {}, None, field, Person)
    assert isinstance(result, mfields.Nested)
    assert result.nested == Address

def test_build_type_with_optional():
    @dataclass
    class Contact:
        email: str

    field = mfields.Field(name="contact", type=Optional[Contact])
    result = build_type(Optional[Contact], {}, None, field, Person)
    assert isinstance(result, mfields.Nested)
    assert result.nested == Contact
    assert result.allow_none

def test_build_type_with_union():
    class PhoneType(Enum):
        HOME = "home"
        WORK = "work"

    @dataclass
    class Contact:
        phone: Union[str, PhoneType]

    field = mfields.Field(name="contact", type=Contact)
    result = build_type(Contact, {}, None, field, Person)
    assert isinstance(result, mfields.Raw)

def test_build_type_with_unknown_type():
    class UnknownType: pass
    field = mfields.Field(name="unknown", type=UnknownType)
    with pytest.warns(UserWarning):
        result = build_type(UnknownType, {}, None, field, Person)
    assert isinstance(result, mfields.Field)

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_build_type_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0.py:44:13: E0602: Undefined variable 'build_type' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0.py:54:13: E0602: Undefined variable 'build_type' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0.py:69:13: E0602: Undefined variable 'build_type' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0.py:76:17: E0602: Undefined variable 'build_type' (undefined-variable)

"""