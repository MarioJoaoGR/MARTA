
import pytest
from isort._vendored.tomli._parser import skip_comment

def test_skip_comment_basic():
    src = "x = 10 # This is a comment\ny = 20"
    pos = 0
    new_pos = skip_comment(src, pos)
    assert new_pos == 14

def test_skip_comment_no_comment():
    src = "x = 10\ny = 20"
    pos = 0
    new_pos = skip_comment(src, pos)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_comment_0.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
___________________________ test_skip_comment_basic ____________________________

    def test_skip_comment_basic():
        src = "x = 10 # This is a comment\ny = 20"
        pos = 0
        new_pos = skip_comment(src, pos)
>       assert new_pos == 14
E       assert 0 == 14

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_comment_0.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_comment_0.py::test_skip_comment_basic
========================= 1 failed, 1 passed in 0.10s ==========================
"""