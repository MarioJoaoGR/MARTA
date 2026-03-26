
import re
from string_utils.manipulation import camel_case_to_snake, is_camel_case, InvalidInputError, is_string

def test_valid_input():
    # Test case for a valid camel case string
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'
    
    # Additional test cases to ensure the function handles various valid camel case strings correctly
    assert camel_case_to_snake('AnotherCamelCaseExample', separator='-') == 'another-camel-case-example'
    assert camel_case_to_snake('Mixed123CamelCaseWithNumbers') == 'mixed123_camel_case_with_numbers'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation_camel_case_to_snake_2_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Test case for a valid camel case string
        assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'
    
        # Additional test cases to ensure the function handles various valid camel case strings correctly
        assert camel_case_to_snake('AnotherCamelCaseExample', separator='-') == 'another-camel-case-example'
>       assert camel_case_to_snake('Mixed123CamelCaseWithNumbers') == 'mixed123_camel_case_with_numbers'
E       AssertionError: assert 'mixed123came..._with_numbers' == 'mixed123_cam..._with_numbers'
E         
E         - mixed123_camel_case_with_numbers
E         ?         -
E         + mixed123camel_case_with_numbers

python-string-utils/Test4DT_tests/test_string_utils_manipulation_camel_case_to_snake_2_test_valid_input.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation_camel_case_to_snake_2_test_valid_input.py::test_valid_input
============================== 1 failed in 0.03s ===============================
"""