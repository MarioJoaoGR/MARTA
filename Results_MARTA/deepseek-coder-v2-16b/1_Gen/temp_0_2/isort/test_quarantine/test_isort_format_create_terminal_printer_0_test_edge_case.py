
from unittest.mock import patch
import sys
import pytest
from isort.format import create_terminal_printer, BasicPrinter, ColoramaPrinter

def test_create_terminal_printer():
    # Test with color enabled and available
    with patch('isort.format.colorama_unavailable', return_value=False):
        printer = create_terminal_printer(color=True)
        assert isinstance(printer, ColoramaPrinter)
    
    # Test with color disabled and available
    with patch('isort.format.colorama_unavailable', return_value=False):
        printer = create_terminal_printer(color=False)
        assert isinstance(printer, BasicPrinter)
    
    # Test with color enabled but colorama unavailable (should not call sys.exit)
    with patch('isort.format.colorama_unavailable', return_value=True):
        with pytest.raises(SystemExit) as e:
            create_terminal_printer(color=True)
        assert e.type == SystemExit
        assert e.value.code == 1

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

isort/Test4DT_tests/test_isort_format_create_terminal_printer_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
_________________________ test_create_terminal_printer _________________________

    def test_create_terminal_printer():
        # Test with color enabled and available
        with patch('isort.format.colorama_unavailable', return_value=False):
>           printer = create_terminal_printer(color=True)

isort/Test4DT_tests/test_isort_format_create_terminal_printer_0_test_edge_case.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

color = True, output = None, error = '', success = ''

    def create_terminal_printer(
        color: bool, output: TextIO | None = None, error: str = "", success: str = ""
    ) -> BasicPrinter:
        if color and colorama_unavailable:
            no_colorama_message = (
                "\n"
                "Sorry, but to use --color (color_output) the colorama python package is required.\n\n"
                "Reference: https://pypi.org/project/colorama/\n\n"
                "You can either install it separately on your system or as the colors extra "
                "for isort. Ex: \n\n"
                "$ pip install isort[colors]\n"
            )
            print(no_colorama_message, file=sys.stderr)
>           sys.exit(1)
E           SystemExit: 1

isort/isort/format.py:151: SystemExit
----------------------------- Captured stderr call -----------------------------

Sorry, but to use --color (color_output) the colorama python package is required.

Reference: https://pypi.org/project/colorama/

You can either install it separately on your system or as the colors extra for isort. Ex: 

$ pip install isort[colors]

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_format_create_terminal_printer_0_test_edge_case.py::test_create_terminal_printer
============================== 1 failed in 0.11s ===============================
"""