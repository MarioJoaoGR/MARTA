
from isort._vendored.tomli._parser import skip_comment, TOMLDecodeError
import pytest

def test_skip_comment():
    # Test case 1: No comment found at the start
    src = "abcdef"
    pos = 0
    assert skip_comment(src, pos) == 0

    # Test case 2: Comment found and skipped until newline character
    src = "abc#def\nghi"
    pos = 0
    assert skip_comment(src, pos) == 6

    # Test case 3: Comment starts within the given position range
    src = "abc#def\nghi"
    pos = 3
    assert skip_comment(src, pos) == 6

    # Test case 4: Invalid input should raise TOMLDecodeError
    src = "abc#invalid\nghi"
    pos = 0
    with pytest.raises(TOMLDecodeError):
        skip_comment(src, pos)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_comment_1_test_invalid_input_error_handling.py F [100%]

=================================== FAILURES ===================================
______________________________ test_skip_comment _______________________________

    def test_skip_comment():
        # Test case 1: No comment found at the start
        src = "abcdef"
        pos = 0
        assert skip_comment(src, pos) == 0
    
        # Test case 2: Comment found and skipped until newline character
        src = "abc#def\nghi"
        pos = 0
>       assert skip_comment(src, pos) == 6
E       AssertionError: assert 0 == 6
E        +  where 0 = skip_comment('abc#def\nghi', 0)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_comment_1_test_invalid_input_error_handling.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_comment_1_test_invalid_input_error_handling.py::test_skip_comment
============================== 1 failed in 0.11s ===============================
"""