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
