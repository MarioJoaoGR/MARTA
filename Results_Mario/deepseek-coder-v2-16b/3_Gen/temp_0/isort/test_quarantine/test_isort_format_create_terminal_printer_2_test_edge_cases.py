
from io import StringIO
import sys
import pytest
from unittest.mock import patch
from isort.format import create_terminal_printer, BasicPrinter, ColoramaPrinter

@patch('isort.format.colorama_unavailable', True)
def test_create_terminal_printer_no_colorama():
    captured_output = StringIO()
    sys.stderr = captured_output
    
    with pytest.raises(SystemExit):
        create_terminal_printer(True, None, "Error message", "Success message")
    
    assert captured_output.getvalue().strip() == (
        "\n"
        "Sorry, but to use --color (color_output) the colorama python package is required.\n\n"
        "Reference: https://pypi.org/project/colorama/\n\n"
        "You can either install it separately on your system or as the colors extra "
        "for isort. Ex: \n\n"
        "$ pip install isort[colors]\n"
    )

@patch('isort.format.colorama_unavailable', False)
def test_create_terminal_printer_with_color():
    output = StringIO()
    result = create_terminal_printer(True, output, "Error message", "Success message")
    
    assert isinstance(result, ColoramaPrinter)
    assert result.output == output
    assert result.error == "Error message"
    assert result.success == "Success message"

def test_create_terminal_printer_without_color():
    output = StringIO()
    result = create_terminal_printer(False, output, "Error message", "Success message")
    
    assert isinstance(result, BasicPrinter)
    assert result.output == output
    assert result.error == "Error message"
    assert result.success == "Success message"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

isort/Test4DT_tests/test_isort_format_create_terminal_printer_2_test_edge_cases.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
___________________ test_create_terminal_printer_no_colorama ___________________

    @patch('isort.format.colorama_unavailable', True)
    def test_create_terminal_printer_no_colorama():
        captured_output = StringIO()
        sys.stderr = captured_output
    
        with pytest.raises(SystemExit):
            create_terminal_printer(True, None, "Error message", "Success message")
    
>       assert captured_output.getvalue().strip() == (
            "\n"
            "Sorry, but to use --color (color_output) the colorama python package is required.\n\n"
            "Reference: https://pypi.org/project/colorama/\n\n"
            "You can either install it separately on your system or as the colors extra "
            "for isort. Ex: \n\n"
            "$ pip install isort[colors]\n"
        )
E       AssertionError: assert 'Sorry, but t...isort[colors]' == '\nSorry, but...ort[colors]\n'
E         
E         - 
E           Sorry, but to use --color (color_output) the colorama python package is required.
E           
E           Reference: https://pypi.org/project/colorama/
E           
E           You can either install it separately on your system or as the colors extra for isort. Ex: ...
E         
E         ...Full output truncated (4 lines hidden), use '-vv' to show

isort/Test4DT_tests/test_isort_format_create_terminal_printer_2_test_edge_cases.py:16: AssertionError
___________________ test_create_terminal_printer_with_color ____________________

    @patch('isort.format.colorama_unavailable', False)
    def test_create_terminal_printer_with_color():
        output = StringIO()
>       result = create_terminal_printer(True, output, "Error message", "Success message")

isort/Test4DT_tests/test_isort_format_create_terminal_printer_2_test_edge_cases.py:28: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

color = True, output = <_io.StringIO object at 0x7fbb5bf9cd30>
error = 'Error message', success = 'Success message'

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
            sys.exit(1)
    
        if not colorama_unavailable:
>           colorama.init(strip=False)
E           NameError: name 'colorama' is not defined

isort/isort/format.py:154: NameError
__________________ test_create_terminal_printer_without_color __________________

    def test_create_terminal_printer_without_color():
        output = StringIO()
        result = create_terminal_printer(False, output, "Error message", "Success message")
    
        assert isinstance(result, BasicPrinter)
        assert result.output == output
>       assert result.error == "Error message"
E       AssertionError: assert error == 'Error message'
E        +  where error = <isort.format.BasicPrinter object at 0x7fbb5c2145d0>.error

isort/Test4DT_tests/test_isort_format_create_terminal_printer_2_test_edge_cases.py:41: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_format_create_terminal_printer_2_test_edge_cases.py::test_create_terminal_printer_no_colorama
FAILED isort/Test4DT_tests/test_isort_format_create_terminal_printer_2_test_edge_cases.py::test_create_terminal_printer_with_color
FAILED isort/Test4DT_tests/test_isort_format_create_terminal_printer_2_test_edge_cases.py::test_create_terminal_printer_without_color
============================== 3 failed in 0.14s ===============================
"""