
import pytest
from string_utils.validation import InvalidInputError

class Test__ISBNChecker:
    def setup(self):
        self.valid_isbn_13 = "9780470059029"
        self.invalid_isbn_13 = "978-0-470-05902-9"
        self.valid_normalized_isbn_13 = "9780470059029"
        self.invalid_normalized_isbn_13 = "978-0-470-05902-9"

    def test_valid_isbn_13(self):
        checker = __ISBNChecker(self.valid_isbn_13)
        assert checker.is_isbn_13() is True

    def test_invalid_isbn_13(self):
        checker = __ISBNChecker("1234567890128")  # This should be invalid as per the length check
        assert checker.is_isbn_13() is False

    def test_normalize_input(self):
        checker = __ISBNChecker(self.invalid_normalized_isbn_13)
        assert checker.input_string == self.valid_normalized_isbn_13

    def test_invalid_input_error(self):
        with pytest.raises(InvalidInputError):
            __ISBNChecker(123456)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation___ISBNChecker_is_isbn_13_1_test_invalid_input_error
python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_1_test_invalid_input_error.py:13:18: E0602: Undefined variable '__ISBNChecker' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_1_test_invalid_input_error.py:17:18: E0602: Undefined variable '__ISBNChecker' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_1_test_invalid_input_error.py:21:18: E0602: Undefined variable '__ISBNChecker' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_1_test_invalid_input_error.py:26:12: E0602: Undefined variable '__ISBNChecker' (undefined-variable)


"""