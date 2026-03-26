
import pytest
from typing import List, Tuple, Set, Dict, Collection
from dataclasses_json.utils import _is_nonstr_collection, _get_type_origin, _issubclass_safe

def test_valid_input_set():
    # Test if a valid set type is recognized as non-string collection
    assert _is_nonstr_collection(Set[int]) == True
    assert _is_nonstr_collection(Set[str]) == True
    assert _is_nonstr_collection(Set[float]) == True
    # Additional tests for other valid set types can be added here
