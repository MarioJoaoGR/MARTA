
import pytest
from string import ascii_lowercase
from unittest.mock import patch
from your_module_name import is_pangram  # Replace 'your_module_name' with the actual module name where `is_pangram` is defined

@pytest.mark.parametrize("input_string", ["The quick brown fox jumps over the lazy dog"])
def test_valid_pangram(input_string):
    assert is_pangram(input_string) == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_pangram_0_test_valid_pangram
python-string-utils/Test4DT_tests/test_string_utils_validation_is_pangram_0_test_valid_pangram.py:5:0: E0401: Unable to import 'your_module_name' (import-error)


"""