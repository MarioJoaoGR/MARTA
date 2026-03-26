
# Module: string_utils.validation
import pytest
from string_utils.manipulation import is_isbn_10

# Test cases for valid ISBN-10 numbers with and without normalization
def test_valid_isbn_10():
    assert is_isbn_10('1506715214') == True
    assert is_isbn_10('150-6715214') == True

# Test cases for invalid ISBN-10 numbers with and without normalization
def test_invalid_isbn_10():
    assert is_isbn_10('1506715214', normalize=False) == False
    assert is_isbn_10('150-6715214', normalize=False) == False
    assert is_isbn_10('9780470059029') == False  # Example of an invalid ISBN-13, not ISBN-10

# Test cases for edge cases
def test_edge_cases():
    # Empty string
    assert is_isbn_10('') == False
    # String with only hyphens
    assert is_isbn_10('---------') == False
    # String with non-digit characters
    assert is_isbn_10('150-671521a') == False

# Test cases for normalization behavior
def test_normalize():
    assert is_isbn_10('150-6715214') == True  # Normalization should ignore hyphens
    assert is_isbn_10('1506715214', normalize=False) == False  # Without normalization, there are hyphens

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_isbn_10_0
python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_10_0.py:4:0: E0611: No name 'is_isbn_10' in module 'string_utils.manipulation' (no-name-in-module)

"""