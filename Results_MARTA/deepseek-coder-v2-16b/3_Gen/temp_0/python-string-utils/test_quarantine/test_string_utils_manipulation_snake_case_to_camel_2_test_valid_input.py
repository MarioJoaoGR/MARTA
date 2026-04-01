
import pytest
from string_utils.manipulation import snake_case_to_camel

def test_valid_input():
    # Test case with valid snake case input
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', separator='-') == 'TheSnakeIsGreen'  # Test with different separator

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation_snake_case_to_camel_2_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Test case with valid snake case input
        assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
        assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
>       assert snake_case_to_camel('the_snake_is_green', separator='-') == 'TheSnakeIsGreen'  # Test with different separator
E       AssertionError: assert 'the_snake_is_green' == 'TheSnakeIsGreen'
E         
E         - TheSnakeIsGreen
E         + the_snake_is_green

python-string-utils/Test4DT_tests/test_string_utils_manipulation_snake_case_to_camel_2_test_valid_input.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation_snake_case_to_camel_2_test_valid_input.py::test_valid_input
============================== 1 failed in 0.03s ===============================
"""