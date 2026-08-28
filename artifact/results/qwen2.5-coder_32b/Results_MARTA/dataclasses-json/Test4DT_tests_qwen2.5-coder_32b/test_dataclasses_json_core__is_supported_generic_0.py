
import pytest
from typing import List, Optional, Union, Dict, Set, Tuple
from enum import Enum
from dataclasses_json.core import _is_supported_generic, _issubclass_safe, _is_collection, _is_optional, is_union_type

# Example class for demonstration
class Color(Enum):
    RED = 1
    GREEN = 2

def test_is_supported_generic_list():
    assert _is_supported_generic(List[int]) == True

def test_is_supported_generic_optional():
    assert _is_supported_generic(Optional[str]) == True

def test_is_supported_generic_union():
    assert _is_supported_generic(Union[int, float]) == True

def test_is_supported_generic_enum():
    assert _is_supported_generic(Color) == True

def test_is_supported_generic_string():
    assert _is_supported_generic(str) == False

def test_is_supported_generic_dict():
    assert _is_supported_generic(Dict[str, int]) == True

def test_is_supported_generic_set():
    assert _is_supported_generic(Set[int]) == True

def test_is_supported_generic_tuple():
    assert _is_supported_generic(Tuple[int, str]) == True
