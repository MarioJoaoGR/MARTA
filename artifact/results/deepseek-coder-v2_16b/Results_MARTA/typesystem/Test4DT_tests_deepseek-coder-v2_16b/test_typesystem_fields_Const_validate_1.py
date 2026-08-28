
import pytest
from typesystem.fields import Const

# Scenario 1: Test initialization with a constant value
def test_init_with_const():
    const_instance = Const(const=42)
    assert const_instance.const == 42

# Scenario 2: Test validation of matching value
def test_validate_matching_value():
    const_instance = Const(const=42)
    validated_value = const_instance.validate(value=42)
    assert validated_value == 42

# Scenario 3: Test validation of non-matching value

# Scenario 4: Test initialization disallowing null values
def test_init_disallow_null():
    with pytest.raises(AssertionError):
        Const(const=None, allow_null=False)

# Scenario 5: Test initialization allowing null values