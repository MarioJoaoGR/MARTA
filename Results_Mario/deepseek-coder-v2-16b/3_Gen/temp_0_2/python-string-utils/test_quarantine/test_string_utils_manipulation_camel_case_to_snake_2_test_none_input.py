
import pytest
from string_utils.manipulation import camel_case_to_snake

def test_none_input():
    # Test when input is None
    assert camel_case_to_snake(None) == None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation_camel_case_to_snake_2_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        # Test when input is None
>       assert camel_case_to_snake(None) == None

python-string-utils/Test4DT_tests/test_string_utils_manipulation_camel_case_to_snake_2_test_none_input.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_string = None, separator = '_'

    def camel_case_to_snake(input_string, separator='_'):
        """
        Convert a camel case string into a snake case one.
        (The original string is returned if is not a valid camel case string)
    
        *Example:*
    
        >>> camel_case_to_snake('ThisIsACamelStringTest') # returns 'this_is_a_camel_case_string_test'
    
        :param input_string: String to convert.
        :type input_string: str
        :param separator: Sign to use as separator.
        :type separator: str
        :return: Converted string.
        """
        if not is_string(input_string):
>           raise InvalidInputError(input_string)
E           string_utils.errors.InvalidInputError: Expected "str", received "NoneType"

python-string-utils/string_utils/manipulation.py:316: InvalidInputError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation_camel_case_to_snake_2_test_none_input.py::test_none_input
============================== 1 failed in 0.03s ===============================
"""