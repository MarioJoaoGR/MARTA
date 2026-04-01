
import pytest
from string_utils.validation import InvalidInputError, is_string

class TestISBNChecker:
    @pytest.mark.parametrize("input_string, normalize, expected", [
        ("978-0-13-235088-4", True, "9780132350884"),
        ("0-13-235088-4", False, "0132350884"),
        (12345, True, InvalidInputError),
        ("invalid_input", True, InvalidInputError)
    ])
    def test_invalid_input(self, input_string, normalize, expected):
        with pytest.raises(InvalidInputError):
            if isinstance(input_string, str):
                checker = __ISBNChecker(input_string, normalize)
                assert checker.input_string == expected
            else:
                raise InvalidInputError("Not a string")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation___ISBNChecker___init___1_test_invalid_input
python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker___init___1_test_invalid_input.py:15:26: E0602: Undefined variable '__ISBNChecker' (undefined-variable)


"""