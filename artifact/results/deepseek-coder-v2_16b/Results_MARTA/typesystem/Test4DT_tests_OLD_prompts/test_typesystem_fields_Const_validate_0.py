
import pytest
from typesystem.fields import Const

def test_valid_initialization():
    const_instance = Const(const=42)
    assert const_instance.const == 42

def test_validate_matching_value():
    const_instance = Const(const=42)
    validated_value = const_instance.validate(value=42)
    assert validated_value == 42


def test_allow_null_initialization():
    with pytest.raises(AssertionError):
        Const(const=None, allow_null=True)