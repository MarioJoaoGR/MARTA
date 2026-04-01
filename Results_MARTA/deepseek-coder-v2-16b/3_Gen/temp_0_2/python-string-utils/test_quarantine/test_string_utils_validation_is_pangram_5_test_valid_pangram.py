
import string
from unittest.mock import patch
import pytest
from your_module_name import is_pangram  # Replace with the actual module name where `is_pangram` function is defined

@pytest.mark.parametrize("input_string, expected", [
    ('The quick brown fox jumps over the lazy dog', True),
    ('hello world', False),
    ('A quick movement of the enemy will jeopardize five gunboats', True),
    ('Sphinx of black quartz, judge my vow', True),
    ('', False),
    (' ', False)
])
@patch('your_module_name.is_full_string')  # Replace with the actual module name where `is_full_string` function is defined
def test_valid_pangram(mock_is_full_string, input_string, expected):
    mock_is_full_string.return_value = True  # Assuming is_full_string always returns True for the purpose of this test
    assert is_pangram(input_string) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_pangram_5_test_valid_pangram
python-string-utils/Test4DT_tests/test_string_utils_validation_is_pangram_5_test_valid_pangram.py:5:0: E0401: Unable to import 'your_module_name' (import-error)


"""