
import pytest
from dataclasses_json import utils as json_utils
from collections import Counter

def test_valid_case_same_type():
    class MyCounter(Counter):
        pass
    
    # Test when type is a subclass of Counter
    assert json_utils._is_counter(MyCounter) == True
    
    # Test when type is not a subclass of Counter
    class NotACounter:
        pass
    
    assert json_utils._is_counter(NotACounter) == False
