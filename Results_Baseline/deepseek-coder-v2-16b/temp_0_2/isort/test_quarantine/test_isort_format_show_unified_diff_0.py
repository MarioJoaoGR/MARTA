
import pytest
from pathlib import Path
from datetime import datetime
from io import StringIO
from isort.format import show_unified_diff, create_terminal_printer, unified_diff

# Test cases for show_unified_diff function
def test_show_unified_diff_basic():
    file_input = "line1\nline2\nline3"
    file_output = "line1\nchanged line2\nline3"
    output = StringIO()
    show_unified_diff(file_input=file_input, file_output=file_output, file_path=None, output=output)
    assert output.getvalue().strip() == (
        "--- \n"
        "+++ changed line2\n"
        "@@ -1,3 +1,3 @@\n"
        " line1\n"
        "-line2\n"
        "+changed line2\n"
        " line3\n"
    )

def test_show_unified_diff_custom_output():
    file_input = "line1\nline2\nline3"
    file_output = "line1\nchanged line2\nline3"
    output = StringIO()
    show_unified_diff(file_input=file_input, file_output=file_output, file_path=None, output=output)
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

isort/Test4DT_tests/test_isort_format_show_unified_diff_0.py F.          [100%]

=================================== FAILURES ===================================
_________________________ test_show_unified_diff_basic _________________________

    def test_show_unified_diff_basic():
        file_input = "line1\nline2\nline3"
        file_output = "line1\nchanged line2\nline3"
        output = StringIO()
        show_unified_diff(file_input=file_input, file_output=file_output, file_path=None, output=output)
>       assert output.getvalue().strip() == (
            "--- \n"
            "+++ changed line2\n"
            "@@ -1,3 +1,3 @@\n"
            " line1\n"
            "-line2\n"
            "+changed line2\n"
            " line3\n"
        )
E       AssertionError: assert '--- :before\...line2\n line3' == '--- \n+++ ch...ne2\n line3\n'
E         
E         - --- 
E         - +++ changed line2
E         + --- :before	2026-03-25 14:42:56.341151
E         + +++ :after	2026-03-25 14:42:56.341164
E           @@ -1,3 +1,3 @@
E            line1...
E         
E         ...Full output truncated (5 lines hidden), use '-vv' to show

isort/Test4DT_tests/test_isort_format_show_unified_diff_0.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_format_show_unified_diff_0.py::test_show_unified_diff_basic
========================= 1 failed, 1 passed in 0.09s ==========================
"""