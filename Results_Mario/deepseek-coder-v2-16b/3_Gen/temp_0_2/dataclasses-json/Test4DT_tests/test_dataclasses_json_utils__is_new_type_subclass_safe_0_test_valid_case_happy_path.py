
import pytest
from dataclasses_json.utils import _is_new_type_subclass_safe

# Define test classes
class A: pass
class B(A): pass
class C: pass
class D(str): pass

def test_valid_case_happy_path():
    assert _is_new_type_subclass_safe(B, A) == True
    assert _is_new_type_subclass_safe(C, int) == False
    assert _is_new_type_subclass_safe(D, str) == True
