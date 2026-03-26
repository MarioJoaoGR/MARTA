
from string_utils.validation import is_string, InvalidInputError
import pytest

@pytest.fixture(name="checker")
def fixture_checker():
    return __ISBNChecker("978-0-13-235088-4", normalize=True)

def test_valid_input_with_normalize_true(checker):
    assert checker.input_string == "9780132350884"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation___ISBNChecker___init___0_test_valid_input_with_normalize_true
python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker___init___0_test_valid_input_with_normalize_true.py:7:11: E0602: Undefined variable '__ISBNChecker' (undefined-variable)

"""