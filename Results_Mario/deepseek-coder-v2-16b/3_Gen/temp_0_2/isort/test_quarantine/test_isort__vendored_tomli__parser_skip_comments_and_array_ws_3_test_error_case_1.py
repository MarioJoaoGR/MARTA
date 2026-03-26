
import pytest
from isort._vendored.tomli._parser import skip_comments_and_array_ws, TOML_WS_AND_NEWLINE

def test_error_case_1():
    src = 'valid string'
    pos = -1
    with pytest.raises(IndexError):
        skip_comments_and_array_ws(src, pos)

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_comments_and_array_ws_3_test_error_case_1.py F [100%]

=================================== FAILURES ===================================
______________________________ test_error_case_1 _______________________________

    def test_error_case_1():
        src = 'valid string'
        pos = -1
>       with pytest.raises(IndexError):
E       Failed: DID NOT RAISE <class 'IndexError'>

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_comments_and_array_ws_3_test_error_case_1.py:8: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_comments_and_array_ws_3_test_error_case_1.py::test_error_case_1
============================== 1 failed in 0.11s ===============================
"""