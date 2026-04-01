
import pytest
from collections import Counter
from dataclasses_json.utils import _is_counter, _get_type_origin, _issubclass_safe

def test_invalid_input():
    none_value = None
    non_type_object = 'not a type'
    
    # Test with None value
    assert not _is_counter(none_value)
    
    # Test with non-type object
    assert not _is_counter(non_type_object)
