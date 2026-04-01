
import pytest
from dataclasses_json.utils import _is_counter, Counter, _get_type_origin, _issubclass_safe

def test_valid_case_subclass():
    class MySubClass(Counter):
        pass
    
    # Test when type is a subclass of Counter
    assert _is_counter(MySubClass) == True
    
    # Test when type is not a subclass of Counter
    class NotACounter(list):
        pass
    
    assert _is_counter(NotACounter) == False
