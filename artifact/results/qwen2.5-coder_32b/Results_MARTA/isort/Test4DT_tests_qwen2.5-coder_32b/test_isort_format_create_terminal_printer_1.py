
import sys
from io import StringIO
import pytest
from isort.format import create_terminal_printer, BasicPrinter, ColoramaPrinter

# Simulate colorama availability
colorama_unavailable = False


def test_create_terminal_printer_color_false_no_colorama():
    global colorama_unavailable
    colorama_unavailable = True  # Ensure colorama is simulated as unavailable
    printer = create_terminal_printer(color=False)
    assert isinstance(printer, BasicPrinter)

def test_create_terminal_printer_color_true_with_colorama():
    global colorama_unavailable
    colorama_unavailable = False  # Simulate colorama being available
    printer = create_terminal_printer(color=True)
    assert isinstance(printer, ColoramaPrinter)

def test_create_terminal_printer_color_false_with_colorama():
    global colorama_unavailable
    colorama_unavailable = False  # Simulate colorama being available
    printer = create_terminal_printer(color=False)
    assert isinstance(printer, BasicPrinter)

def test_create_terminal_printer_output_file():
    output_file = StringIO()
    printer = create_terminal_printer(color=False, output=output_file)
    assert isinstance(printer, BasicPrinter)