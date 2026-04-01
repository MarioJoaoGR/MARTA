
import pytest
from string import ascii_lowercase
from unittest.mock import patch
from your_module_name import is_pangram  # Replace 'your_module_name' with the actual module name where `is_pangram` is defined

@pytest.mark.parametrize("input_string, expected", [
    ('', False),
    ('The quick brown fox jumps over the lazy dog', True),
    ('hello world', False),
])
def test_is_pangram(input_string, expected):
    assert is_pangram(input_string) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_pangram_2_test_empty_string
python-string-utils/Test4DT_tests/test_string_utils_validation_is_pangram_2_test_empty_string.py:5:0: E0401: Unable to import 'your_module_name' (import-error)

"""