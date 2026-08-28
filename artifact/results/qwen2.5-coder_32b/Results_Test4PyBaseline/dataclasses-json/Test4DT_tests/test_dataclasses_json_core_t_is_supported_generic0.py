# Module: dataclasses_json.core
import pytest
from typing import List, Optional, Union, Dict, Set, Tuple
from enum import Enum
from dataclasses_json.core import _is_supported_generic

# Define an enumeration for testing
class Color(Enum):
    RED = 1
    GREEN = 2

def test_is_supported_generic_collection():
    assert _is_supported_generic(List[int]) is True
    assert _is_supported_generic(Dict[str, int]) is True
    assert _is_supported_generic(Set[float]) is True
    assert _is_supported_generic(Tuple[int, str]) is True

def test_is_supported_generic_optional():
    assert _is_supported_generic(Optional[str]) is True
    assert _is_supported_generic(Optional[Color]) is True
    assert _is_supported_generic(Optional[List[int]]) is True

def test_is_supported_generic_union():
    assert _is_supported_generic(Union[int, str]) is True
    assert _is_supported_generic(Union[Color, int]) is True
    assert _is_supported_generic(Union[str, List[int], Dict[str, float]]) is True

def test_is_supported_generic_enum():
    assert _is_supported_generic(Color) is True

def test_is_supported_generic_string():
    assert _is_supported_generic(str) is False

def test_is_supported_generic_non_collection():
    assert _is_supported_generic(int) is False
    assert _is_supported_generic(float) is False
    assert _is_supported_generic(bool) is False

def test_is_supported_generic_custom_class():
    class CustomClass:
        pass

    assert _is_supported_generic(CustomClass) is False

def test_is_supported_generic_nested_types():
    assert _is_supported_generic(Optional[List[Optional[int]]]) is True
    assert _is_supported_generic(Union[str, Optional[List[int]], Dict[str, Union[float, int]]]) is True
