
import pytest
from dataclasses import dataclass

# Define a hypothetical dataclass for testing
@dataclass
class MyClass:
    param1: int = 1
    param2: int = 2

def _is_new_type_subclass_safe(cls, classinfo):
    super_type = getattr(cls, "__supertype__", None)
    if super_type:
        return _is_new_type_subclass_safe(super_type, classinfo)
    try:
        return issubclass(cls, classinfo)
    except Exception:
        return False

# Test cases for _is_new_type_subclass_safe function
def test_is_new_type_subclass_safe_with_supertype():
    # Create a superclass and subclass to test recursion with __supertype__
    class A: pass
    class B(A): 
        __supertype__ = A
    
    assert _is_new_type_subclass_safe(B, A) == True

def test_is_not_new_type_subclass_safe():
    # Test a case where the class is not a subclass of the given type
    class C: pass
    