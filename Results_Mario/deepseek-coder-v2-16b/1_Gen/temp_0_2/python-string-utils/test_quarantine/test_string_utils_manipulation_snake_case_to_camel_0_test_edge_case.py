
import pytest
from string_utils.manipulation import snake_case_to_camel, InvalidInputError

def test_edge_cases():
    # Test None input
    assert snake_case_to_camel(None) == None
    
    # Test empty string input
    assert snake_case_to_camel("") == ""
    
    # Test non-snake case strings
    assert snake_case_to_camel("invalidSnakeCase") == "invalidSnakeCase"
    assert snake_case_to_camel("anotherInvalidString") == "anotherInvalidString"
    
    # Test valid snake case strings with different upper_case_first values
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=True) == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    
    # Test valid snake case strings with different separators
    assert snake_case_to_camel('the-snake-is-green', separator='-') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the.snake.is.green', separator='.') == 'TheSnakeIsGreen'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation_snake_case_to_camel_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test None input
>       assert snake_case_to_camel(None) == None

python-string-utils/Test4DT_tests/test_string_utils_manipulation_snake_case_to_camel_0_test_edge_case.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_string = None, upper_case_first = True, separator = '_'

    def snake_case_to_camel(input_string: str, upper_case_first: bool = True, separator: str = '_') -> str:
        """
        Convert a snake case string into a camel case one.
        (The original string is returned if is not a valid snake case string)
    
        *Example:*
    
        >>> snake_case_to_camel('the_snake_is_green') # returns 'TheSnakeIsGreen'
    
        :param input_string: String to convert.
        :type input_string: str
        :param upper_case_first: True to turn the first letter into uppercase (default).
        :type upper_case_first: bool
        :param separator: Sign to use as separator (default to "_").
        :type separator: str
        :return: Converted string
        """
        if not is_string(input_string):
>           raise InvalidInputError(input_string)
E           string_utils.errors.InvalidInputError: Expected "str", received "NoneType"

python-string-utils/string_utils/manipulation.py:342: InvalidInputError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation_snake_case_to_camel_0_test_edge_case.py::test_edge_cases
============================== 1 failed in 0.05s ===============================
"""