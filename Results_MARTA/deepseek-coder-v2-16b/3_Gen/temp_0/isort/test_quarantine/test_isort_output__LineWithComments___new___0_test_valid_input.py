
from isort.output import _LineWithComments

def test_valid_input():
    line_with_comments = _LineWithComments("print('Hello, World!')", ["This is a simple print statement."])
    assert line_with_comments.value == "print('Hello, World!')"
    assert line_with_comments.comments == ["This is a simple print statement."]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_output__LineWithComments___new___0_test_valid_input
isort/Test4DT_tests/test_isort_output__LineWithComments___new___0_test_valid_input.py:6:11: E1101: Instance of '_LineWithComments' has no 'value' member (no-member)


"""