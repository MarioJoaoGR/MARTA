
import pytest
from string_utils.validation import __ISBNChecker, InvalidInputError

def test_invalid_input_error_case():
    # Test when input is not a string
    with pytest.raises(InvalidInputError) as excinfo:
        checker = __ISBNChecker(12345)
    assert str(excinfo.value) == "Input must be a string, got <class 'int'>"

    # Test when input is not a valid ISBN-13 number
    with pytest.raises(InvalidInputError) as excinfo:
        checker = __ISBNChecker("9780470059028")  # Invalid ISBN-13 number
    assert str(excinfo.value) == "Input must be a string, got <class 'str'>"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_0_test_invalid_input_error_case.py F [100%]

=================================== FAILURES ===================================
________________________ test_invalid_input_error_case _________________________

    def test_invalid_input_error_case():
        # Test when input is not a string
        with pytest.raises(InvalidInputError) as excinfo:
            checker = __ISBNChecker(12345)
>       assert str(excinfo.value) == "Input must be a string, got <class 'int'>"
E       assert 'Expected "st...eceived "int"' == "Input must b...<class 'int'>"
E         
E         - Input must be a string, got <class 'int'>
E         + Expected "str", received "int"

python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_0_test_invalid_input_error_case.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker_is_isbn_13_0_test_invalid_input_error_case.py::test_invalid_input_error_case
============================== 1 failed in 0.03s ===============================
"""