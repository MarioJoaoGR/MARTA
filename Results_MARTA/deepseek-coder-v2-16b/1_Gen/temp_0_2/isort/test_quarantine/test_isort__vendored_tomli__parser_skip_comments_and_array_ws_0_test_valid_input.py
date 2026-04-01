
from isort._vendored.tomli._parser import skip_comments_and_array_ws
from isort._vendored.tomli._parser import Pos
import pytest

def test_valid_input():
    src = "  # This is a comment\n  123  # Another comment"
    pos = 0
    new_pos = skip_comments_and_array_ws(src, pos)
    assert new_pos == 4  # After skipping the whitespace and comments, we should be at position 4.

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_comments_and_array_ws_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        src = "  # This is a comment\n  123  # Another comment"
        pos = 0
        new_pos = skip_comments_and_array_ws(src, pos)
>       assert new_pos == 4  # After skipping the whitespace and comments, we should be at position 4.
E       assert 24 == 4

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_comments_and_array_ws_0_test_valid_input.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_comments_and_array_ws_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.10s ===============================
"""