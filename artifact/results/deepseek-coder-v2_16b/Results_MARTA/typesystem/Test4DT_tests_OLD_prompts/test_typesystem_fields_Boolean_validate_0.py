
import pytest
from unittest.mock import patch
from typesystem.fields import Boolean

# Test validate method with a valid boolean string input
def test_validate_valid_boolean_string():
    bool_validator = Boolean(allow_null=True)
    assert bool_validator.validate("true") == True
    assert bool_validator.validate("on") == True
    assert bool_validator.validate("1") == True

# Test validate method with an invalid boolean string input in strict mode
def test_validate_invalid_boolean_string_strict():
    bool_validator = Boolean(allow_null=True)
    with pytest.raises(Exception):
        bool_validator.validate("not a boolean")

# Test validate method with a valid integer input
def test_validate_valid_integer():
    bool_validator = Boolean(allow_null=True)
    assert bool_validator.validate(1) == True
    assert bool_validator.validate(0) == False

# Test validate method with an invalid type in strict mode
def test_validate_invalid_type_strict():
    bool_validator = Boolean(allow_null=True)
    with pytest.raises(Exception):
        bool_validator.validate("1", strict=True)

# Test validate method with None and allow_null set to True
def test_validate_none_with_allow_null():
    bool_validator = Boolean(allow_null=True)
    assert bool_validator.validate(None) is None

# Test validate method with a null string input in strict mode

# Test validate method with an invalid value that can be coerced to a boolean
def test_validate_invalid_value_coerce():
    bool_validator = Boolean(allow_null=True)
    assert bool_validator.validate("false") == False
    assert bool_validator.validate("off") == False
    assert bool_validator.validate("0") == False