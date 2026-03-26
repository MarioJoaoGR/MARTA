
import pytest
from pymonet.task import Task

def test_reject():
    # Test rejecting a valid value
    task = Task.reject("error")
    assert task is not None
    
    # Test rejecting None
    rejected_none = Task.reject(None)
    assert rejected_none is not None
    
    # Test rejecting an empty list
    rejected_empty_list = Task.reject([])
    assert rejected_empty_list is not None
    
    # Test rejecting a zero (int)
    rejected_zero = Task.reject(0)
    assert rejected_zero is not None
    
    # Test rejecting a float
    rejected_float = Task.reject(1.23)
    assert rejected_float is not None
    
    # Test rejecting a boolean (True)
    rejected_true = Task.reject(True)
    assert rejected_true is not None
    
    # Test rejecting a boolean (False)
    rejected_false = Task.reject(False)
    assert rejected_false is not None
    
    # Test rejecting a string
    rejected_string = Task.reject("test")
    assert rejected_string is not None
