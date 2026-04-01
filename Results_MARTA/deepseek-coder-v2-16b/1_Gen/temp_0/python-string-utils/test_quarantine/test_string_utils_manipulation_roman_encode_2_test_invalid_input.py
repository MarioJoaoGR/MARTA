
import pytest
from roman_numerals import roman_encode  # Assuming this is the module where your function lives

def test_invalid_input():
    with pytest.raises(ValueError):
        roman_encode("0")  # Invalid because it's zero
        roman_encode(-1)   # Invalid because it's negative
        roman_encode(4000) # Invalid because it's out of range

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation_roman_encode_2_test_invalid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation_roman_encode_2_test_invalid_input.py:3:0: E0401: Unable to import 'roman_numerals' (import-error)

"""