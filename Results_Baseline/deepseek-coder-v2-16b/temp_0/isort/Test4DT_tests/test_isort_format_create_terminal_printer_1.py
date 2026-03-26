
# Module: isort.format
import sys
from io import StringIO

import pytest

from isort.format import BasicPrinter, ColoramaPrinter, create_terminal_printer

try:
    from colorama import Fore, Style  # noqa: F401
except ImportError:
    class Fore: pass
    class Style: pass
    colorama_unavailable = True
else:
    colorama_unavailable = False

@pytest.mark.skipif(colorama_unavailable, reason="Colorama is unavailable")
def test_create_terminal_printer_with_color():
    output = StringIO()
    create_terminal_printer(True, output, "Error message", "Success message")
    assert output.getvalue().strip() == Style.RESET_ALL + Fore.RED + "Error message" + Style.RESET_ALL + " Success message"

@pytest.mark.skipif(colorama_unavailable, reason="Colorama is unavailable")
def test_create_terminal_printer_without_color():
    output = StringIO()
    create_terminal_printer(False, output, "Error message", "Success message")
    assert output.getvalue().strip() == "Error message Success message"

@pytest.mark.skipif(colorama_unavailable, reason="Colorama is unavailable")
def test_create_terminal_printer_default_output():
    original_stdout = sys.stdout
    try:
        output = StringIO()
        sys.stdout = output
        create_terminal_printer(True)
        assert output.getvalue().strip() == Style.RESET_ALL + Fore.RED + "Error message" + Style.RESET_ALL + " Success message"
    finally:
        sys.stdout = original_stdout

@pytest.mark.skipif(colorama_unavailable, reason="Colorama is unavailable")
def test_create_terminal_printer_invalid_color():
    with pytest.raises(SystemExit):
        create_terminal_printer(True, None, "Error message", "Success message")

@pytest.mark.skipif(not colorama_unavailable, reason="Colorama is available")
def test_create_terminal_printer_without_colorama():
    with pytest.raises(SystemExit):
        create_terminal_printer(True, None, "Error message", "Success message")

# Additional Test Case for Colorama Unavailability Handling
@pytest.mark.skipif(not colorama_unavailable, reason="Colorama is available")
def test_create_terminal_printer_colorama_unavailable():
    original_stderr = sys.stderr
    with pytest.raises(SystemExit):
        # Redirect stderr to capture the error message
        captured_output = StringIO()
        sys.stderr = captured_output
        create_terminal_printer(True, None, "Error message", "Success message")
        assert captured_output.getvalue().strip() == (
            "\n"
            "Sorry, but to use --color (color_output) the colorama python package is required.\n\n"
            "Reference: https://pypi.org/project/colorama/\n\n"
            "You can either install it separately on your system or as the colors extra "
            "for isort. Ex: \n\n"
            "$ pip install isort[colors]\n"
        )
    sys.stderr = original_stderr
