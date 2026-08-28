
import pytest
from typesystem.fields import Const

# Test initialization with a specific constant value
def test_initialization_with_specific_constant():
    c = Const(const=42)
    assert c.const == 42

# Test validation without strict mode (should pass)
def test_validate_without_strict_mode():
    c = Const(const=42)
    result = c.validate(value=42)
    assert result == 42

# Test initialization allowing only null values (should raise an assertion error with the correct message)
def test_initialization_with_allow_null():
    with pytest.raises(AssertionError) as e:
        Const(const=None, allow_null=True)