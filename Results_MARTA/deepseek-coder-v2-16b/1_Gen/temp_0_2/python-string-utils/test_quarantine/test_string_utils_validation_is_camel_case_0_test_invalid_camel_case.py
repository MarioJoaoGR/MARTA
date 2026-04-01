
from string_utils.validation import is_camel_case

def test_invalid_camel_case():
    # Test cases for invalid camel case strings
    invalid_cases = [
        "MyString",  # Valid camel case
        "myString",  # Invalid camel case (starts with lowercase)
        "1MyString",  # Invalid camel case (starts with a number)
        "MYSTRING",  # Invalid camel case (all uppercase)
        "my_string",  # Invalid camel case (contains underscore)
        "my string",  # Invalid camel case (contains space)
    ]
    
    for case in invalid_cases:
        assert not is_camel_case(case), f"Expected {case} to be considered as invalid camel case."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_camel_case_0_test_invalid_camel_case.py F [100%]

=================================== FAILURES ===================================
___________________________ test_invalid_camel_case ____________________________

    def test_invalid_camel_case():
        # Test cases for invalid camel case strings
        invalid_cases = [
            "MyString",  # Valid camel case
            "myString",  # Invalid camel case (starts with lowercase)
            "1MyString",  # Invalid camel case (starts with a number)
            "MYSTRING",  # Invalid camel case (all uppercase)
            "my_string",  # Invalid camel case (contains underscore)
            "my string",  # Invalid camel case (contains space)
        ]
    
        for case in invalid_cases:
>           assert not is_camel_case(case), f"Expected {case} to be considered as invalid camel case."
E           AssertionError: Expected MyString to be considered as invalid camel case.
E           assert not True
E            +  where True = is_camel_case('MyString')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_camel_case_0_test_invalid_camel_case.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_camel_case_0_test_invalid_camel_case.py::test_invalid_camel_case
============================== 1 failed in 0.03s ===============================
"""