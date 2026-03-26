
import re
from string_utils.validation import is_full_string

def test_invalid_characters():
    input_string = 'My blog post title'
    assert not is_slug(input_string), "Expected False for invalid characters in slug"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_slug_7_test_invalid_characters
python-string-utils/Test4DT_tests/test_string_utils_validation_is_slug_7_test_invalid_characters.py:7:15: E0602: Undefined variable 'is_slug' (undefined-variable)


"""