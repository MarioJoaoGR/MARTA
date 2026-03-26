
import pytest
from string_utils.validation import InvalidInputError, is_string

class Test__ISBNChecker:
    def setup(self):
        self.checker = __ISBNChecker("978-0-13-235088-4")

    def test_valid_isbn_10(self):
        assert self.checker.is_isbn_10() == True

    def test_invalid_isbn_10(self):
        with pytest.raises(InvalidInputError):
            checker = __ISBNChecker("invalid input")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation___ISBNChecker_is_isbn_10_1_test_error_invalid_input
python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_10_1_test_error_invalid_input.py:7:23: E0602: Undefined variable '__ISBNChecker' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_10_1_test_error_invalid_input.py:14:22: E0602: Undefined variable '__ISBNChecker' (undefined-variable)


"""