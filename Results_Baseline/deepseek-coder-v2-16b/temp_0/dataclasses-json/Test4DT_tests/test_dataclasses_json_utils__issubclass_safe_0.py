
import pytest
from dataclasses_json.utils import _issubclass_safe

# Test cases for _issubclass_safe function

def test_issubclass_safe_true():
    class A: pass
    class B(A): pass
    assert _issubclass_safe(B, A) == True

def test_issubclass_safe_false():
    class C: pass
    assert _issubclass_safe(C, int) == False

def test_issubclass_safe_true_new_type():
    class D(str): pass