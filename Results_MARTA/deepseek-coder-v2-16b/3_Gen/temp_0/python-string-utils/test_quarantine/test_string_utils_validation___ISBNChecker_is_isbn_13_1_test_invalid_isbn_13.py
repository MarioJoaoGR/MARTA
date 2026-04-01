
import pytest
from unittest.mock import patch, MagicMock
from string_utils.validation import __ISBNChecker

@pytest.mark.parametrize("input_string", ["9780470059029", "978-0-470-05902-9"])
def test_invalid_isbn_13(input_string):
    with patch('string_utils.validation.__ISBNChecker', autospec=True) as mock_checker:
        checker = mock_checker.return_value
        checker.input_string = input_string.replace('-', '') if '-' in input_string else input_string
        
        assert not checker.is_isbn_13()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_1_test_invalid_isbn_13.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________ test_invalid_isbn_13[9780470059029] ______________________

input_string = '9780470059029'

    @pytest.mark.parametrize("input_string", ["9780470059029", "978-0-470-05902-9"])
    def test_invalid_isbn_13(input_string):
        with patch('string_utils.validation.__ISBNChecker', autospec=True) as mock_checker:
            checker = mock_checker.return_value
            checker.input_string = input_string.replace('-', '') if '-' in input_string else input_string
    
>           assert not checker.is_isbn_13()
E           AssertionError: assert not <MagicMock name='__ISBNChecker().is_isbn_13()' id='4368984736'>
E            +  where <MagicMock name='__ISBNChecker().is_isbn_13()' id='4368984736'> = <MagicMock name='__ISBNChecker().is_isbn_13' spec='function' id='4368989680'>()
E            +    where <MagicMock name='__ISBNChecker().is_isbn_13' spec='function' id='4368989680'> = <NonCallableMagicMock name='__ISBNChecker()' spec='__ISBNChecker' id='4368688576'>.is_isbn_13

python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_1_test_invalid_isbn_13.py:12: AssertionError
___________________ test_invalid_isbn_13[978-0-470-05902-9] ____________________

input_string = '978-0-470-05902-9'

    @pytest.mark.parametrize("input_string", ["9780470059029", "978-0-470-05902-9"])
    def test_invalid_isbn_13(input_string):
        with patch('string_utils.validation.__ISBNChecker', autospec=True) as mock_checker:
            checker = mock_checker.return_value
            checker.input_string = input_string.replace('-', '') if '-' in input_string else input_string
    
>           assert not checker.is_isbn_13()
E           AssertionError: assert not <MagicMock name='__ISBNChecker().is_isbn_13()' id='4369430320'>
E            +  where <MagicMock name='__ISBNChecker().is_isbn_13()' id='4369430320'> = <MagicMock name='__ISBNChecker().is_isbn_13' spec='function' id='4369429792'>()
E            +    where <MagicMock name='__ISBNChecker().is_isbn_13' spec='function' id='4369429792'> = <NonCallableMagicMock name='__ISBNChecker()' spec='__ISBNChecker' id='4369423888'>.is_isbn_13

python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_1_test_invalid_isbn_13.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_1_test_invalid_isbn_13.py::test_invalid_isbn_13[9780470059029]
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_1_test_invalid_isbn_13.py::test_invalid_isbn_13[978-0-470-05902-9]
============================== 2 failed in 0.03s ===============================
"""