
# Module: dataclasses_json.utils
import pytest
from dataclasses import dataclass
from typing import Dict, Any
import inspect
import functools

# Define a hypothetical dataclass for testing
@dataclass
class MyClass:
    param1: int = 1
    param2: int = 2

def _is_new_type_subclass_safe(subclass, superclass):
    return issubclass(subclass, superclass)

def test_is_new_type_subclass_safe():
    class A: pass
    class B(A): pass
    
    assert _is_new_type_subclass_safe(B, A) == True
    assert _is_new_type_subclass_safe(MyClass, MyClass) == True  # Assuming MyClass.__supertype__ is set correctly for this test

def test_is_not_new_type_subclass_safe():
    class C: pass
    
    assert _is_new_type_subclass_safe(C, int) == False

def test_is_new_type_subclass_safe_with_inheritance():
    class D(str): pass
    
    assert _is_new_type_subclass_safe(D, str) == True

# Add more tests to cover edge cases and ensure robustness
