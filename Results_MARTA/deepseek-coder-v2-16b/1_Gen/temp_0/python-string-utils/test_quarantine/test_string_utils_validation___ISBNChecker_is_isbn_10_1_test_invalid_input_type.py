
import pytest
from string_utils.validation import is_string, InvalidInputError
from unittest.mock import patch

class Test__ISBNChecker:
    def setup(self):
        self.checker = __ISBNChecker("9780470059029")

    @patch('string_utils.validation.is_string')
    def test_invalid_input_type(self, mock_is_string):
        mock_is_string.return_value = False
        with pytest.raises(InvalidInputError):
            __ISBNChecker("not a string")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation___ISBNChecker_is_isbn_10_1_test_invalid_input_type
python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_10_1_test_invalid_input_type.py:8:23: E0602: Undefined variable '__ISBNChecker' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_10_1_test_invalid_input_type.py:14:12: E0602: Undefined variable '__ISBNChecker' (undefined-variable)

"""