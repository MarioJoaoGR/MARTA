# Module: dataclasses_json.utils
import pytest
from typing import Optional, List, Any
from dataclasses_json.utils import _is_optional

# Helper functions for testing
def _issubclass_safe(cls, classinfo):
    return isinstance(cls, type) and issubclass(cls, classinfo)

def _hasargs(cls, *args):
    from inspect import signature
    sig = signature(cls)
    return any(param.default == param.empty for param in sig.parameters.values())

# Test cases for _is_optional function
def test_is_optional_with_optional():
    assert _is_optional(Optional[int]) is True, "Expected Optional[int] to be considered optional"

def test_is_optional_with_list():
    assert _is_optional(List[str]) is False, "Expected List[str] not to be considered optional"

def test_is_optional_with_any():
    assert _is_optional(Any) is True, "Expected Any to be considered optional"

# Additional edge cases
def test_is_optional_with_primitive_type():
    assert _is_optional(int) is False, "Expected int not to be considered optional"

def test_is_optional_with_none():
    class CustomOptional:
        pass
    custom_optional = CustomOptional()
    assert _is_optional(custom_optional.__class__) is False, "Expected a custom type not to be considered optional"

if __name__ == "__main__":
    pytest.main()
