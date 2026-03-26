
import pytest
from dataclasses import dataclass
from typing import Dict, Any, Tuple, Type

# Import the function from its module
from dataclasses_json.utils import _isinstance_safe

def test_isinstance_safe_with_single_type():
    assert _isinstance_safe(42, int) == True
    assert _isinstance_safe("hello", str) == True
    assert _isinstance_safe(3.14, float) == True
    assert _isinstance_safe(None, (int, float)) == False
    assert _isinstance_safe([], list) == True