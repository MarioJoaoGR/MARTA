
import pytest
from dataclasses_json.utils import _issubclass_safe

# Define classes A and B
class A: pass
class B(A): pass

def test_valid_case_1():
    assert _issubclass_safe(B, A) == True
