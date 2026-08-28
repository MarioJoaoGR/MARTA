
import pytest
from string_utils.validation import __ISBNChecker, InvalidInputError

# Helper function to simulate is_string check for testing purposes
def is_string(obj):
    return isinstance(obj, str)

class Test__ISBNChecker:
    
    def test_valid_isbn_13(self):
        checker = __ISBNChecker('9780451450526')
        assert checker.input_string == '9780451450526'
        assert checker.is_isbn_13() is True
    
    def test_non_normalized_isbn_13(self):
        checker = __ISBNChecker('978-0-451-45052-6', normalize=False)
        assert checker.input_string == '978-0-451-45052-6'
        assert checker.is_isbn_13() is True
    
    def test_invalid_input_isbn_13(self):
        with pytest.raises(InvalidInputError):
            __ISBNChecker(9780451450526)  # This should raise InvalidInputError since the input is not a string
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_validation___ISBNChecker_is_isbn_13_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_____________________ Test__ISBNChecker.test_valid_isbn_13 _____________________

self = <test_string_utils_validation___ISBNChecker_is_isbn_13_0.Test__ISBNChecker object at 0x7f1eedb70a60>

    def test_valid_isbn_13(self):
>       checker = __ISBNChecker('9780451450526')
E       NameError: name '_Test__ISBNChecker__ISBNChecker' is not defined

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_validation___ISBNChecker_is_isbn_13_0.py:12: NameError
________________ Test__ISBNChecker.test_non_normalized_isbn_13 _________________

self = <test_string_utils_validation___ISBNChecker_is_isbn_13_0.Test__ISBNChecker object at 0x7f1eedb70b80>

    def test_non_normalized_isbn_13(self):
>       checker = __ISBNChecker('978-0-451-45052-6', normalize=False)
E       NameError: name '_Test__ISBNChecker__ISBNChecker' is not defined

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_validation___ISBNChecker_is_isbn_13_0.py:17: NameError
_________________ Test__ISBNChecker.test_invalid_input_isbn_13 _________________

self = <test_string_utils_validation___ISBNChecker_is_isbn_13_0.Test__ISBNChecker object at 0x7f1eedb72860>

    def test_invalid_input_isbn_13(self):
        with pytest.raises(InvalidInputError):
>           __ISBNChecker(9780451450526)  # This should raise InvalidInputError since the input is not a string
E           NameError: name '_Test__ISBNChecker__ISBNChecker' is not defined

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_validation___ISBNChecker_is_isbn_13_0.py:23: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_validation___ISBNChecker_is_isbn_13_0.py::Test__ISBNChecker::test_valid_isbn_13
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_validation___ISBNChecker_is_isbn_13_0.py::Test__ISBNChecker::test_non_normalized_isbn_13
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_validation___ISBNChecker_is_isbn_13_0.py::Test__ISBNChecker::test_invalid_input_isbn_13
============================== 3 failed in 0.06s ===============================
"""