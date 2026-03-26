
import pytest
from dataclasses_json.utils import _isinstance_safe

# Test cases for _isinstance_safe function
def test_isinstance_safe_with_single_type():
    assert _isinstance_safe([1, 2, 3], list) == True
    assert _isinstance_safe(42, int) == True