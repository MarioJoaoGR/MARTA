
import pytest
from roman_numerals import roman_encode  # Assuming the function is in a module named 'roman_numerals'

def test_invalid_integer_out_of_range():
    input_number = 4000
    with pytest.raises(ValueError):
        roman_encode(input_number)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation_roman_encode_1_test_invalid_integer_out_of_range
python-string-utils/Test4DT_tests/test_string_utils_manipulation_roman_encode_1_test_invalid_integer_out_of_range.py:3:0: E0401: Unable to import 'roman_numerals' (import-error)


"""