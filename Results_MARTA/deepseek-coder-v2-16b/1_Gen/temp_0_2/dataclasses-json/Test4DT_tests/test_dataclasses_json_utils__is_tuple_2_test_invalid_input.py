
import pytest
from dataclasses_json.utils import _is_tuple
from typing import Tuple, List

def test_invalid_input():
    # Test with an invalid input type (not a class)
    assert not _is_tuple(42)  # int is not a tuple-like structure
    
    # Test with a valid but non-tuple type (e.g., List)
    my_list = List[int]
    assert not _is_tuple(my_list)  # List is not a Tuple
