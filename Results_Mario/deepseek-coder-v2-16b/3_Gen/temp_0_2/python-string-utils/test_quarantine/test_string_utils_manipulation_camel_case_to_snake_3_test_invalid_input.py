
import re
from string_utils.manipulation import camel_case_to_snake, is_camel_case, InvalidInputError

def test_invalid_input():
    # Test with an empty string
    assert camel_case_to_snake("") == ""
    
    # Test with a string that is not in camel case
    assert camel_case_to_snake("this_is_not_camel_case") == "this_is_not_camel_case"
    
    # Test with a string containing numbers and mixed cases
    assert camel_case_to_snake("CamelCaseWithNumbers123") == "camel_case_with_numbers123"
    
    # Test with a string that contains special characters
    assert camel_case_to_snake("CamelCase!@#String") == "camel_case__string"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation_camel_case_to_snake_3_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Test with an empty string
        assert camel_case_to_snake("") == ""
    
        # Test with a string that is not in camel case
        assert camel_case_to_snake("this_is_not_camel_case") == "this_is_not_camel_case"
    
        # Test with a string containing numbers and mixed cases
        assert camel_case_to_snake("CamelCaseWithNumbers123") == "camel_case_with_numbers123"
    
        # Test with a string that contains special characters
>       assert camel_case_to_snake("CamelCase!@#String") == "camel_case__string"
E       AssertionError: assert 'CamelCase!@#String' == 'camel_case__string'
E         
E         - camel_case__string
E         + CamelCase!@#String

python-string-utils/Test4DT_tests/test_string_utils_manipulation_camel_case_to_snake_3_test_invalid_input.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation_camel_case_to_snake_3_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.04s ===============================
"""