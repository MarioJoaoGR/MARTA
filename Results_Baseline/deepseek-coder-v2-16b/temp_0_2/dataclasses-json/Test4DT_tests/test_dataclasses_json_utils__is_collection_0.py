
import pytest
from typing import List, Set, Optional
from dataclasses_json.utils import _is_collection

def test_is_collection_builtin():
    assert _is_collection(List[int]) == True  # Built-in collection type
    assert _is_collection(Set[int]) == True   # Built-in collection type

def test_is_collection_custom():
    class MyCustomCollection: pass
    assert _is_collection(MyCustomCollection) == False  # Custom non-collection class

def test_is_collection_optional():
    from typing import Optional