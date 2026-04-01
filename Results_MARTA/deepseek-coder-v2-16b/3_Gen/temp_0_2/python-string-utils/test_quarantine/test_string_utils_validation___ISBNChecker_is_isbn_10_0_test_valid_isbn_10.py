
import pytest
from string_utils.validation import is_string, InvalidInputError
from unittest.mock import patch

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

@pytest.mark.parametrize("isbn, expected", [
    ("0471606957", True),   # Valid ISBN-10
    ("978-0-471-60695-7", True),  # Valid ISBN-10 with hyphens
    ("0471606958", False),  # Invalid ISBN-10 (checksum fails)
    ("978-0-471-60695-8", False),  # Invalid ISBN-10 with hyphens (checksum fails)
    ("invalidinput", False),  # Invalid input that is not a string
    ("047160695X", True),   # Valid ISBN-10 with 'X' as the last digit
])
def test_is_isbn_10(isbn, expected):
    with patch('string_utils.validation.is_string', return_value=True):  # Mock is_string to always return True for simplicity
        checker = __ISBNChecker(isbn)
        assert checker.is_isbn_10() == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 6 items

python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_10_0_test_valid_isbn_10.py F [ 16%]
F...F                                                                    [100%]

=================================== FAILURES ===================================
_______________________ test_is_isbn_10[0471606957-True] _______________________

isbn = '0471606957', expected = True

    @pytest.mark.parametrize("isbn, expected", [
        ("0471606957", True),   # Valid ISBN-10
        ("978-0-471-60695-7", True),  # Valid ISBN-10 with hyphens
        ("0471606958", False),  # Invalid ISBN-10 (checksum fails)
        ("978-0-471-60695-8", False),  # Invalid ISBN-10 with hyphens (checksum fails)
        ("invalidinput", False),  # Invalid input that is not a string
        ("047160695X", True),   # Valid ISBN-10 with 'X' as the last digit
    ])
    def test_is_isbn_10(isbn, expected):
        with patch('string_utils.validation.is_string', return_value=True):  # Mock is_string to always return True for simplicity
            checker = __ISBNChecker(isbn)
>           assert checker.is_isbn_10() == expected
E           assert False == True
E            +  where False = is_isbn_10()
E            +    where is_isbn_10 = <Test4DT_tests.test_string_utils_validation___ISBNChecker_is_isbn_10_0_test_valid_isbn_10.__ISBNChecker object at 0x1028df790>.is_isbn_10

python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_10_0_test_valid_isbn_10.py:39: AssertionError
___________________ test_is_isbn_10[978-0-471-60695-7-True] ____________________

isbn = '978-0-471-60695-7', expected = True

    @pytest.mark.parametrize("isbn, expected", [
        ("0471606957", True),   # Valid ISBN-10
        ("978-0-471-60695-7", True),  # Valid ISBN-10 with hyphens
        ("0471606958", False),  # Invalid ISBN-10 (checksum fails)
        ("978-0-471-60695-8", False),  # Invalid ISBN-10 with hyphens (checksum fails)
        ("invalidinput", False),  # Invalid input that is not a string
        ("047160695X", True),   # Valid ISBN-10 with 'X' as the last digit
    ])
    def test_is_isbn_10(isbn, expected):
        with patch('string_utils.validation.is_string', return_value=True):  # Mock is_string to always return True for simplicity
            checker = __ISBNChecker(isbn)
>           assert checker.is_isbn_10() == expected
E           assert False == True
E            +  where False = is_isbn_10()
E            +    where is_isbn_10 = <Test4DT_tests.test_string_utils_validation___ISBNChecker_is_isbn_10_0_test_valid_isbn_10.__ISBNChecker object at 0x102982080>.is_isbn_10

python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_10_0_test_valid_isbn_10.py:39: AssertionError
_______________________ test_is_isbn_10[047160695X-True] _______________________

isbn = '047160695X', expected = True

    @pytest.mark.parametrize("isbn, expected", [
        ("0471606957", True),   # Valid ISBN-10
        ("978-0-471-60695-7", True),  # Valid ISBN-10 with hyphens
        ("0471606958", False),  # Invalid ISBN-10 (checksum fails)
        ("978-0-471-60695-8", False),  # Invalid ISBN-10 with hyphens (checksum fails)
        ("invalidinput", False),  # Invalid input that is not a string
        ("047160695X", True),   # Valid ISBN-10 with 'X' as the last digit
    ])
    def test_is_isbn_10(isbn, expected):
        with patch('string_utils.validation.is_string', return_value=True):  # Mock is_string to always return True for simplicity
            checker = __ISBNChecker(isbn)
>           assert checker.is_isbn_10() == expected
E           assert False == True
E            +  where False = is_isbn_10()
E            +    where is_isbn_10 = <Test4DT_tests.test_string_utils_validation___ISBNChecker_is_isbn_10_0_test_valid_isbn_10.__ISBNChecker object at 0x102983670>.is_isbn_10

python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_10_0_test_valid_isbn_10.py:39: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_10_0_test_valid_isbn_10.py::test_is_isbn_10[0471606957-True]
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_10_0_test_valid_isbn_10.py::test_is_isbn_10[978-0-471-60695-7-True]
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_10_0_test_valid_isbn_10.py::test_is_isbn_10[047160695X-True]
========================= 3 failed, 3 passed in 0.03s ==========================
"""