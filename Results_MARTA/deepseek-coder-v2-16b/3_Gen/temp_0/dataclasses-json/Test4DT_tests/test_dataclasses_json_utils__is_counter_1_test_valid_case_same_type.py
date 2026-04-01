
import pytest
from dataclasses_json.utils import _is_counter, _get_type_origin, _issubclass_safe
from collections import Counter

def test_valid_case_same_type():
    class MyCounter(Counter):
        pass
    
    # Test when type is a subclass of Counter
    assert _is_counter(MyCounter) == True
    
    # Test when type is not a subclass of Counter
    assert _is_counter(list) == False
