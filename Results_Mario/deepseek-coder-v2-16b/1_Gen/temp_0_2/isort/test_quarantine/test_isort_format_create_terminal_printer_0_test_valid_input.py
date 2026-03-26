
import pytest
from unittest.mock import patch
import sys
from io import StringIO
from isort.format import create_terminal_printer, BasicPrinter, ColoramaPrinter
import colorama

@pytest.mark.skipif(sys.platform == "win32", reason="Colorama not supported on Windows")
def test_valid_input():
    with patch('isort.format.colorama_unavailable', return_value=False):
        # Test when color is True
        output = StringIO()
        printer = create_terminal_printer(color=True, output=output)
        assert isinstance(printer, ColoramaPrinter)
        
        # Test when color is False
        output = StringIO()
        printer = create_terminal_printer(color=False, output=output)
        assert isinstance(printer, BasicPrinter)
        
        # Test with custom error and success messages
        output = StringIO()
        printer = create_terminal_printer(color=True, error="Custom Error", success="Custom Success", output=output)
        assert isinstance(printer, ColoramaPrinter)
        assert printer.error == "Custom Error"
        assert printer.success == "Custom Success"
        
        # Test when colorama is not available
        with patch('isort.format.colorama_unavailable', return_value=True):
            captured_output = StringIO()
            sys.stderr = captured_output
            with pytest.raises(SystemExit) as excinfo:
                create_terminal_printer(color=True)
            assert "Sorry, but to use --color" in captured_output.getvalue()
            assert excinfo.type == SystemExit
            sys.stderr = sys.__stderr__

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_format_create_terminal_printer_0_test_valid_input
isort/Test4DT_tests/test_isort_format_create_terminal_printer_0_test_valid_input.py:7:0: E0401: Unable to import 'colorama' (import-error)


"""