
import re
from typing import Any

def is_snake_case(input_string: Any, separator: str = '_') -> bool:
    """
    Checks if a string is formatted as "snake case".

    A string is considered snake case when:
    - it's composed only by lowercase/uppercase letters and digits
    - it contains at least one underscore (or provided separator)
    - it does not start with a number

    *Examples:*

    >>> is_snake_case('foo_bar_baz') # returns true
    >>> is_snake_case('foo') # returns false

    :param input_string: String to test.
    :type input_string: str
    :param separator: String to use as separator.
    :type separator: str
    :return: True for a snake case string, false otherwise.
    """
    if is_full_string(input_string):
        re_map = {
            '_': SNAKE_CASE_TEST_RE,
            '-': SNAKE_CASE_TEST_DASH_RE
        }
        re_template = r'([a-z]+\d*{sign}[a-z\d{sign}]*|{sign}+[a-z\d]+[a-z\d{sign}]*)'
        r = re_map.get(
            separator,
            re.compile(re_template.format(sign=re.escape(separator)), re.IGNORECASE)
        )

        return r.match(input_string) is not None

    return False

# Test case for invalid input types
def test_invalid_input_types():
    # Test with non-string type (int)
    assert not is_snake_case(12345, '_')  # Should raise a TypeError
    
    # Test with None type
    assert not is_snake_case(None, '_')  # Should raise a TypeError
    
    # Test with list type
    assert not is_snake_case(['foo', 'bar'], '_')  # Should raise a TypeError

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_snake_case_1_test_error_case
python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_1_test_error_case.py:25:7: E0602: Undefined variable 'is_full_string' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_1_test_error_case.py:27:17: E0602: Undefined variable 'SNAKE_CASE_TEST_RE' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_1_test_error_case.py:28:17: E0602: Undefined variable 'SNAKE_CASE_TEST_DASH_RE' (undefined-variable)


"""