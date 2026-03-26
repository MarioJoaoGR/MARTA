
from isort.format import BasicPrinter
import sys
from io import TextIOBase
from unittest.mock import patch, MagicMock
import pytest

def test_basicprinter_init():
    error_msg = "An error occurred"
    success_msg = "Operation successful"
    
    with patch('sys.stdout', new=MagicMock()) as mock_stdout:
        printer = BasicPrinter(error_msg, success_msg)
        
        assert printer.error_message == error_msg
        assert printer.success_message == success_msg
        assert isinstance(printer.output, TextIOBase)

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

isort/Test4DT_tests/test_isort_format_BasicPrinter___init___0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
____________________________ test_basicprinter_init ____________________________

    def test_basicprinter_init():
        error_msg = "An error occurred"
        success_msg = "Operation successful"
    
        with patch('sys.stdout', new=MagicMock()) as mock_stdout:
            printer = BasicPrinter(error_msg, success_msg)
    
            assert printer.error_message == error_msg
            assert printer.success_message == success_msg
>           assert isinstance(printer.output, TextIOBase)
E           AssertionError: assert False
E            +  where False = isinstance(<MagicMock id='139726563599312'>, TextIOBase)
E            +    where <MagicMock id='139726563599312'> = <isort.format.BasicPrinter object at 0x7f14a0304610>.output

isort/Test4DT_tests/test_isort_format_BasicPrinter___init___0_test_edge_cases.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_format_BasicPrinter___init___0_test_edge_cases.py::test_basicprinter_init
============================== 1 failed in 0.10s ===============================
"""