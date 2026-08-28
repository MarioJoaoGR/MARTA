
import sys
from io import StringIO
import pytest
from isort.format import create_terminal_printer, BasicPrinter, ColoramaPrinter

# Simulate colorama availability
colorama_unavailable = False


def test_create_terminal_printer_with_color():
    global colorama_unavailable
    colorama_unavailable = False  # Ensure colorama is available for this test

    printer = create_terminal_printer(color=True)
    assert isinstance(printer, ColoramaPrinter)

def test_create_terminal_printer_without_color():
    printer = create_terminal_printer(color=False)
    assert isinstance(printer, BasicPrinter)

