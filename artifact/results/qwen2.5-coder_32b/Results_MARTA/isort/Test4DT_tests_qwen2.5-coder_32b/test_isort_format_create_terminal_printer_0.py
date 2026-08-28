
import sys
from io import StringIO
import pytest
from unittest.mock import patch

# Assuming these are the correct imports from isort.format
from isort.format import create_terminal_printer, ColoramaPrinter, BasicPrinter

# Global variable to simulate colorama availability
colorama_unavailable = False

def test_create_terminal_printer_color_enabled():
    global colorama_unavailable
    colorama_unavailable = False  # Simulate colorama is available
    printer = create_terminal_printer(color=True)
    assert isinstance(printer, ColoramaPrinter)

def test_create_terminal_printer_color_disabled():
    global colorama_unavailable
    colorama_unavailable = False  # Simulate colorama is available
    printer = create_terminal_printer(color=False)
    assert isinstance(printer, BasicPrinter)


def test_create_terminal_printer_with_custom_output():
    global colorama_unavailable
    colorama_unavailable = False  # Simulate colorama is available
    output = StringIO()
    printer = create_terminal_printer(color=True, output=output)
    assert isinstance(printer, ColoramaPrinter)
    assert printer.output == output

def test_create_terminal_printer_without_color_with_custom_output():
    global colorama_unavailable
    colorama_unavailable = False  # Simulate colorama is available
    output = StringIO()
    printer = create_terminal_printer(color=False, output=output)
    assert isinstance(printer, BasicPrinter)
    assert printer.output == output