
from isort._vendored.tomli._parser import skip_comment

def test_skip_comment():
    # Test when there is no comment
    src = "abcdef"
    pos = 0
    assert skip_comment(src, pos) == 0
    
    # Test when a comment is found at the start
    src = "abc#def\nghi"
    pos = 0
    assert skip_comment(src, pos) == 6
    
    # Test when a comment is found within the string
    src = "abcdef#ghi\njkl"
    pos = 0
    assert skip_comment(src, pos) == 6

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_comment_2_test_none_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_skip_comment _______________________________

    def test_skip_comment():
        # Test when there is no comment
        src = "abcdef"
        pos = 0
        assert skip_comment(src, pos) == 0
    
        # Test when a comment is found at the start
        src = "abc#def\nghi"
        pos = 0
>       assert skip_comment(src, pos) == 6
E       AssertionError: assert 0 == 6
E        +  where 0 = skip_comment('abc#def\nghi', 0)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_comment_2_test_none_input.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_comment_2_test_none_input.py::test_skip_comment
============================== 1 failed in 0.13s ===============================
"""