
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_valid_input():
    # Test with a valid string
    formatter = __StringFormatter("Hello,world!")
    assert formatter._StringFormatter__ensure_left_space_only(formatter, r'(?<=\w)(\W)') == " Hello,world!"

    # Test with another valid string to ensure it handles multiple matches correctly
    formatter2 = __StringFormatter("This is a test! Keep going.")
    assert formatter2._StringFormatter__ensure_left_space_only(formatter2, r'(?<=\w)(\W)') == " This is a test! Keep going."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___ensure_left_space_only_1_test_valid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___ensure_left_space_only_1_test_valid_input.py:8:11: E1101: Instance of '__StringFormatter' has no '_StringFormatter__ensure_left_space_only' member (no-member)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___ensure_left_space_only_1_test_valid_input.py:12:11: E1101: Instance of '__StringFormatter' has no '_StringFormatter__ensure_left_space_only' member (no-member)


"""