
import pytest
from dataclasses_json.utils import _issubclass_safe, _is_new_type, _is_new_type_subclass_safe

# Define classes A and B for the test
class A: pass
class B(A): pass

def test_valid_case_1():
    # Test if class B is a subclass of class A
    assert _issubclass_safe(B, A) == True
    
    # Define another unrelated class C for testing
    class C: pass
    
    # Test if class C is not a subclass of int
    assert _issubclass_safe(C, int) == False
    
    # Define a subclass of str for further testing
    class D(str): pass
    
    # Test if class D is a subclass of str
    assert _issubclass_safe(D, str) == True
