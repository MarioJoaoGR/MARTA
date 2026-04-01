
import pytest
from string_utils.manipulation import snake_case_to_camel
from custom_exceptions import InvalidInputError

def test_valid_case():
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', separator='-') == 'TheSnakeIsGreen'
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False, separator='-') == 'theSnakeIsGreen'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation_snake_case_to_camel_0_test_valid_case
python-string-utils/Test4DT_tests/test_string_utils_manipulation_snake_case_to_camel_0_test_valid_case.py:4:0: E0401: Unable to import 'custom_exceptions' (import-error)


"""