
import pytest
from typesystem.fields import Const

# Test cases for the Const class
def test_init_with_valid_const():
    const = Const(const=42)
    assert const.const == 42

def test_init_with_invalid_kwargs():
    with pytest.raises(AssertionError):
        Const(const=1, allow_null=True)

def test_validate_matching_value():
    const = Const(const=42)
    result = const.validate(value=42)
    assert result == 42

def test_validate_non_matching_value_strict_mode():
    const = Const(const=42)
    with pytest.raises(Exception):
        const.validate(value=1, strict=True)

def test_validate_null_value_not_allowed():
    const = Const(const=None)
    with pytest.raises(Exception):
        const.validate(value=None, strict=False)

# Additional tests for the validate method in different scenarios
@pytest.mark.parametrize("value, expected", [(42, 42), (None, None)])
def test_validate_matching_value_non_strict_mode(value, expected):
    const = Const(const=expected)
    result = const.validate(value=value)
    assert result == expected

@pytest.mark.parametrize("value", [42, None])
def test_validate_null_value_strict_mode(value):
    const = Const(const=None)
    with pytest.raises(Exception):
        const.validate(value=value, strict=True)
