
# Module: string_utils.generation
# test_string_utils.py
from string_utils import validate  # Fixed typo in module name and added missing import
import pytest

def test_validate_valid_positive_integer():
    assert validate(25, 'number') is None

def test_validate_valid_negative_integer_with_allow_negative():
    with pytest.raises(ValueError) as exc_info:
        validate(-5, 'number', allow_negative=True)
    assert str(exc_info.value) == '"number" must be an integer in the range 1-3999'

def test_validate_invalid_string():
    with pytest.raises(ValueError) as exc_info:
        validate('not an int', 'number')
    assert str(exc_info.value) == '"number" must be an integer in the range 1-3999'

def test_validate_valid_zero():
    with pytest.raises(ValueError) as exc_info:
        validate(0, 'number')
    assert str(exc_info.value) == '"number" must be an integer in the range 1-3999'

def test_validate_valid_large_positive_integer():
    assert validate(3999, 'number') is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_generation_validate_0
python-string-utils/Test4DT_tests/test_string_utils_generation_validate_0.py:4:0: E0611: No name 'validate' in module 'string_utils' (no-name-in-module)

"""