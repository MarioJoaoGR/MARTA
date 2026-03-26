
import re
from string_utils.validation import is_camel_case

def test_valid_camel_case():
    # Test a valid camel case string
    assert is_camel_case('MyString') == True
    
    # Test an invalid camel case string
    assert is_camel_case('myString') == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_camel_case_0_test_valid_camel_case.py F [100%]

=================================== FAILURES ===================================
____________________________ test_valid_camel_case _____________________________

    def test_valid_camel_case():
        # Test a valid camel case string
        assert is_camel_case('MyString') == True
    
        # Test an invalid camel case string
>       assert is_camel_case('myString') == False
E       AssertionError: assert True == False
E        +  where True = is_camel_case('myString')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_camel_case_0_test_valid_camel_case.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_camel_case_0_test_valid_camel_case.py::test_valid_camel_case
============================== 1 failed in 0.03s ===============================
"""