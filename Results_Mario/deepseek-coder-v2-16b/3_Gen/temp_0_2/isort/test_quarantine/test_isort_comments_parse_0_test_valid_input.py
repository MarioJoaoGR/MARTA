
from isort.comments import parse

def test_valid_input():
    # Test cases with valid inputs as described in the docstring examples
    assert parse("import os  # This line imports the OS module").strip() == ('import os', 'This line imports the OS module').strip()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_comments_parse_0_test_valid_input
isort/Test4DT_tests/test_isort_comments_parse_0_test_valid_input.py:6:11: E1101: Instance of 'tuple' has no 'strip' member (no-member)
isort/Test4DT_tests/test_isort_comments_parse_0_test_valid_input.py:6:76: E1101: Instance of 'tuple' has no 'strip' member (no-member)


"""