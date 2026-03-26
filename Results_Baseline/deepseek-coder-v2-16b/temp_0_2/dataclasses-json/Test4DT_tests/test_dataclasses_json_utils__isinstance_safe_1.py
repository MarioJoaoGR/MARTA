
import pytest
from typing import Tuple, Type

# Import the function from its module
from dataclasses_json.utils import _isinstance_safe

def test_isinstance_safe_with_single_type():
    assert _isinstance_safe(42, int) == True
    assert _isinstance_safe("hello", str) == True
    assert _isinstance_safe(3.14, float) == True
    assert _isinstance_safe(None, (int, float)) == False
    assert _isinstance_safe([], list) == True

def test_isinstance_safe_with_multiple_types():
    # Test with a tuple of types
    assert _isinstance_safe(42, (int, str)) == True
    assert _isinstance_safe("hello", (int, str)) == True
    assert _isinstance_safe(3.14, (int, float)) == True
    # Corrected assertion to match expected behavior