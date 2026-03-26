
import pytest
from isort.output import is_comment

def test_valid_input():
    assert is_comment(" # This is a comment") == True
    assert is_comment("This is not a comment") == False
    assert is_comment(None) == False
    assert is_comment("") == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_output_is_comment_0_test_valid_input
isort/Test4DT_tests/test_isort_output_is_comment_0_test_valid_input.py:3:0: E0611: No name 'is_comment' in module 'isort.output' (no-name-in-module)


"""