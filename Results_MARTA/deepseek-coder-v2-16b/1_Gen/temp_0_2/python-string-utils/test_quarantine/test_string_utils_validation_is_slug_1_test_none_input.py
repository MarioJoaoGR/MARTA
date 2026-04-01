
import re
from typing import Any

def is_slug(input_string: Any, separator: str = '-') -> bool:
    """
    Checks if a given string is a slug (as created by `slugify()`).

    *Examples:*

    >>> is_slug('my-blog-post-title') # returns true
    >>> is_slug('My blog post title') # returns false

    :param input_string: String to check.
    :type input_string: str
    :param separator: Join sign used by the slug.
    :type separator: str
    :return: True if slug, false otherwise.
    """
    if not is_full_string(input_string):
        return False

    rex = r'^([a-z\d]+' + re.escape(separator) + r'*?)*[a-z\d]$'

    return re.match(rex, input_string) is not None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_slug_1_test_none_input
python-string-utils/Test4DT_tests/test_string_utils_validation_is_slug_1_test_none_input.py:20:11: E0602: Undefined variable 'is_full_string' (undefined-variable)


"""