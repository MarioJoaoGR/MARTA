
import pytest
from dataclasses_json.utils import _is_new_type_subclass_safe

# Define the classes A and B as described in the setup
class A: pass
class B(A): pass

def test_valid_case_1():
    assert _is_new_type_subclass_safe(B, A) == True
