
import pytest
from dataclasses import dataclass

# Define a hypothetical dataclass for testing
@dataclass
class MyClass:
    param1: int = 1
    param2: int = 2

def _is_new_type_subclass_safe(cls, classinfo):
    if hasattr(cls, "__supertype__"):
        return _is_new_type_subclass_safe(getattr(cls, "__supertype__"), classinfo)
    else:
        try:
            return issubclass(cls, classinfo)
        except Exception:
            return False

# Test cases for _is_new_type_subclass_safe
def test_is_new_type_subclass_safe_basic():
    class A: pass
    class B(A): pass
    
    assert _is_new_type_subclass_safe(B, A) == True

def test_is_not_new_type_subclass_safe():
    class C: pass
    
    assert _is_new_type_subclass_safe(C, int) == False

def test_is_new_type_subclass_safe_with_inheritance():
    class D(str): pass
    
    assert _is_new_type_subclass_safe(D, str) == True

# Test cases for the recursive check with __supertype__ attribute
def test_recursive_check_with_supertype():
    class A: pass
    class B(A): pass
    class C(B): 
        __supertype__ = A
    
    assert _is_new_type_subclass_safe(C, A) == True

def test_recursive_check_without_supertype():
    class A: pass
    class B(A): pass
    class C(B): pass  # No __supertype__ attribute
    