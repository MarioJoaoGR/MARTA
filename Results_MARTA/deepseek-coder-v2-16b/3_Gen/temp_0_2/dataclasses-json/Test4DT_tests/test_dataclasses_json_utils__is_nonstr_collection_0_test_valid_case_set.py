
import pytest
from typing import Set, List, Dict, Tuple
from collections.abc import Collection
from dataclasses_json.utils import _is_nonstr_collection, _get_type_origin, _issubclass_safe

def test_valid_case_set():
    # Test if a set type is recognized as non-string collection
    assert _is_nonstr_collection(Set[int]) == True
    assert _is_nonstr_collection(List[int]) == True  # List is also a non-string collection
    assert _is_nonstr_collection(Dict[str, int]) == True  # Dict is also a non-string collection
    assert _is_nonstr_collection(Tuple[int, ...]) == True  # Tuple is also a non-string collection
    
    # Test if other types are not recognized as non-string collections
    assert _is_nonstr_collection(int) == False
    assert _is_nonstr_collection(str) == False
    assert _is_nonstr_collection(float) == False
