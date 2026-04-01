
import pytest
from isort._vendored.tomli._parser import skip_comments_and_array_ws, TOML_WS_AND_NEWLINE

def test_valid_case_2():
    src = "   \t# this is a comment\nanother line with spaces"
    pos = 0
    result = skip_comments_and_array_ws(src, pos)
    assert result == 21

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_comments_and_array_ws_1_test_valid_case_2.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_case_2 _______________________________

    def test_valid_case_2():
        src = "   \t# this is a comment\nanother line with spaces"
        pos = 0
        result = skip_comments_and_array_ws(src, pos)
>       assert result == 21
E       assert 24 == 21

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_comments_and_array_ws_1_test_valid_case_2.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_comments_and_array_ws_1_test_valid_case_2.py::test_valid_case_2
============================== 1 failed in 0.10s ===============================
"""