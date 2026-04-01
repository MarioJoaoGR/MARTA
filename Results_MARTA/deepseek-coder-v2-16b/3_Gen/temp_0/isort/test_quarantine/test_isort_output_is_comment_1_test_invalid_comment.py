
from isort.output import is_comment

def test_invalid_comment():
    assert not is_comment("This is not a comment")  # False
    assert is_comment("# This is a comment")       # True
    assert not is_comment(None)                   # False
    assert is_comment(" # This is a comment")      # True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_output_is_comment_1_test_invalid_comment
isort/Test4DT_tests/test_isort_output_is_comment_1_test_invalid_comment.py:2:0: E0611: No name 'is_comment' in module 'isort.output' (no-name-in-module)


"""