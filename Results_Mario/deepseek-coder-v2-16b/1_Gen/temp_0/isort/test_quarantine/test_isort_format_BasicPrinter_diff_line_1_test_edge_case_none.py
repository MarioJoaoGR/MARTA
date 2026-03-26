
import pytest
from isort.format import BasicPrinter

@pytest.fixture
def printer():
    return BasicPrinter(error='ERROR', success='SUCCESS')

def test_diff_line(printer, capsys):
    line = "This is a sample line."
    printer.diff_line(line)
    captured = capsys.readouterr()
    assert captured.out == line  # No need to add newline here as the method does not automatically append one

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

isort/Test4DT_tests/test_isort_format_BasicPrinter_diff_line_1_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
________________________________ test_diff_line ________________________________

printer = <isort.format.BasicPrinter object at 0x7f5ebf26a6d0>
capsys = <_pytest.capture.CaptureFixture object at 0x7f5ebf26bb50>

    def test_diff_line(printer, capsys):
        line = "This is a sample line."
        printer.diff_line(line)
        captured = capsys.readouterr()
>       assert captured.out == line  # No need to add newline here as the method does not automatically append one
E       AssertionError: assert '' == 'This is a sample line.'
E         
E         - This is a sample line.

isort/Test4DT_tests/test_isort_format_BasicPrinter_diff_line_1_test_edge_case_none.py:13: AssertionError
----------------------------- Captured stdout call -----------------------------
This is a sample line.
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_format_BasicPrinter_diff_line_1_test_edge_case_none.py::test_diff_line
============================== 1 failed in 0.10s ===============================
"""