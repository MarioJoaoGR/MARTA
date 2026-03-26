
import pytest
from string_utils.validation import InvalidInputError, is_string

class __ISBNChecker:
    def __init__(self, input_string: str, normalize: bool = True):
        if not is_string(input_string):
            raise InvalidInputError(f"Expected 'str', received {type(input_string).__name__}")

        self.input_string = input_string.replace('-', '') if normalize else input_string

    def is_isbn_10(self) -> bool:
        if len(self.input_string) == 10:
            product = 0

            try:
                for index, digit in enumerate(self.input_string):
                    product += int(digit) * (index + 1)

                return product % 11 == 0

            except ValueError:
                pass

        return False

def test_invalid_input_type():
    with pytest.raises(InvalidInputError) as exc_info:
        checker = __ISBNChecker(12345)
    
    assert str(exc_info.value) == "Expected 'str', received 12345"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_10_1_test_invalid_input_type.py F [100%]

=================================== FAILURES ===================================
___________________________ test_invalid_input_type ____________________________

    def test_invalid_input_type():
        with pytest.raises(InvalidInputError) as exc_info:
            checker = __ISBNChecker(12345)
    
>       assert str(exc_info.value) == "Expected 'str', received 12345"
E       assert 'Expected "st...eceived "str"' == "Expected 'st...eceived 12345"
E         
E         - Expected 'str', received 12345
E         ?          ^   ^           ^^^^^
E         + Expected "str", received "str"
E         ?          ^   ^           ^^^^^

python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_10_1_test_invalid_input_type.py:31: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_10_1_test_invalid_input_type.py::test_invalid_input_type
============================== 1 failed in 0.04s ===============================
"""