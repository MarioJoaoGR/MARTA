
from isort._vendored.tomli._parser import skip_comment
from isort._vendor.tomli._parser import Pos

def test_no_comment():
    src = "print('Hello, World!')"
    pos = 0
    new_pos = skip_comment(src, pos)
    assert new_pos == len(src), f"Expected position to be at the end of the string after skipping a comment, but got {new_pos}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_skip_comment_0_test_no_comment
isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_comment_0_test_no_comment.py:3:0: E0401: Unable to import 'isort._vendor.tomli._parser' (import-error)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_comment_0_test_no_comment.py:3:0: E0611: No name '_vendor' in module 'isort' (no-name-in-module)


"""