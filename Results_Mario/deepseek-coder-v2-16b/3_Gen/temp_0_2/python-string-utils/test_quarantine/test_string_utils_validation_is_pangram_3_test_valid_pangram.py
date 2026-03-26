
import string
from unittest.mock import patch
import pytest
from your_module_name import is_pangram  # Replace with the actual module name where `is_pangram` function is defined

@pytest.mark.parametrize("input_string, expected", [
    ('The quick brown fox jumps over the lazy dog', True),
    ('hello world', False)
])
def test_valid_pangram(input_string, expected):
    assert is_pangram(input_string) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_pangram_3_test_valid_pangram
python-string-utils/Test4DT_tests/test_string_utils_validation_is_pangram_3_test_valid_pangram.py:5:0: E0401: Unable to import 'your_module_name' (import-error)


"""