
import pytest
from typing import Optional, Union, List, Any
from enum import Enum
from dataclasses_json.core import _is_supported_generic

# Helper functions for testing (assuming these are defined elsewhere in the module)
def _issubclass_safe(cls, class_or_tuple):
    try:
        return issubclass(cls, class_or_tuple)
    except TypeError:
        return False

def _is_collection(cls):
    from collections import abc
    return isinstance(cls, type) and issubclass(cls, abc.Collection)

def _is_optional(cls):
    if hasattr(cls, '__origin__'):
        origin = cls.__origin__
        if origin == Optional:
            return True
    return False

def is_union_type(cls):
    from typing import Union
    if hasattr(cls, '__args__') and len(cls.__args__) > 1:
        for arg in cls.__args__:
            if not _is_supported_generic(arg):
                return False
        return True
    return False

# Test cases for _is_supported_generic function
def test_is_optional():
    class CustomType: pass
    assert not _is_supported_generic(CustomType)
    OptionalInt = Optional[int]
    assert _is_supported_generic(OptionalInt)

def test_is_union_type():
    IntUnionStr = Union[int, str]
    assert _is_supported_generic(IntUnionStr)
    class CustomType: pass
    assert not _is_supported_generic(CustomType)

def test_is_enum():
    class MyEnum(Enum): pass
    assert _is_supported_generic(MyEnum)
    assert not _is_supported_generic(int)

def test_not_str():
    class CustomType: pass
    assert not _is_supported_generic(CustomType)
