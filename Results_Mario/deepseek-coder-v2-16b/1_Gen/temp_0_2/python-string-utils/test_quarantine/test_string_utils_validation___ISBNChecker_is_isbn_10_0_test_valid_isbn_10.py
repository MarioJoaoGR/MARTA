
import pytest
from string_utils.validation import InvalidInputError, is_string

class __ISBNChecker:
    def __init__(self, input_string: str, normalize: bool = True):
        if not is_string(input_string):
            raise InvalidInputError(input_string)

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

# Test cases for __ISBNChecker.is_isbn_10
def test_valid_isbn_10():
    checker = __ISBNChecker("978-3-16-148410-0")
    assert checker.is_isbn_10() == True, "Expected valid ISBN-10 to be recognized as true"

def test_invalid_isbn_10():
    checker = __ISBNChecker("9780470059028", normalize=False)
    assert checker.is_isbn_10() == False, "Expected invalid ISBN-10 to be recognized as false"

def test_invalid_input_type():
    with pytest.raises(InvalidInputError):
        __ISBNChecker(12345)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_10_0_test_valid_isbn_10.py F [ 33%]
..                                                                       [100%]

=================================== FAILURES ===================================
______________________________ test_valid_isbn_10 ______________________________

    def test_valid_isbn_10():
        checker = __ISBNChecker("978-3-16-148410-0")
>       assert checker.is_isbn_10() == True, "Expected valid ISBN-10 to be recognized as true"
E       AssertionError: Expected valid ISBN-10 to be recognized as true
E       assert False == True
E        +  where False = is_isbn_10()
E        +    where is_isbn_10 = <Test4DT_tests.test_string_utils_validation___ISBNChecker_is_isbn_10_0_test_valid_isbn_10.__ISBNChecker object at 0x1023fead0>.is_isbn_10

python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_10_0_test_valid_isbn_10.py:30: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_10_0_test_valid_isbn_10.py::test_valid_isbn_10
========================= 1 failed, 2 passed in 0.04s ==========================
"""