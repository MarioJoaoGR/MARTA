
import re
from string_utils.manipulation import camel_case_to_snake, is_camel_case, is_string
from string_utils.errors import InvalidInputError

def test_invalid_camel_to_snake():
    input_string = 'ThisIsNotACamelString'
    expected_output = 'ThisIsNotACamelString'  # Since it's not camel case, the original string should be returned

    result = camel_case_to_snake(input_string)

    assert result == expected_output

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation_camel_case_to_snake_6_test_invalid_camel_to_snake.py F [100%]

=================================== FAILURES ===================================
_________________________ test_invalid_camel_to_snake __________________________

    def test_invalid_camel_to_snake():
        input_string = 'ThisIsNotACamelString'
        expected_output = 'ThisIsNotACamelString'  # Since it's not camel case, the original string should be returned
    
        result = camel_case_to_snake(input_string)
    
>       assert result == expected_output
E       AssertionError: assert 'this_is_not_a_camel_string' == 'ThisIsNotACamelString'
E         
E         - ThisIsNotACamelString
E         + this_is_not_a_camel_string

python-string-utils/Test4DT_tests/test_string_utils_manipulation_camel_case_to_snake_6_test_invalid_camel_to_snake.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation_camel_case_to_snake_6_test_invalid_camel_to_snake.py::test_invalid_camel_to_snake
============================== 1 failed in 0.03s ===============================
"""