
import pytest
from dataclasses_json.utils import _is_new_type_subclass_safe

# Define classes as per the setup
class C: pass
class D(C): __supertype__ = C

def test_valid_case_2():
    # Test if a class is not a subclass of multiple classes
    assert _is_new_type_subclass_safe(D, C) == True
