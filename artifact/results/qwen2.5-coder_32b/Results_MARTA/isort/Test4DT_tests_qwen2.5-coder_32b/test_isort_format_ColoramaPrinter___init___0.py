
import pytest
from io import StringIO
import colorama
from isort.format import ColoramaPrinter

def test_ColoramaPrinter___init___default_output():
    printer = ColoramaPrinter()
    
    assert printer.ERROR == f"{colorama.Fore.RED}ERROR{colorama.Style.RESET_ALL}"
    assert printer.SUCCESS == f"{colorama.Fore.GREEN}SUCCESS{colorama.Style.RESET_ALL}"

def test_ColoramaPrinter___init___custom_output():
    output_stream = StringIO()
    printer = ColoramaPrinter(output=output_stream)
    
    assert printer.ERROR == f"{colorama.Fore.RED}ERROR{colorama.Style.RESET_ALL}"
    assert printer.SUCCESS == f"{colorama.Fore.GREEN}SUCCESS{colorama.Style.RESET_ALL}"

def test_ColoramaPrinter_ADDED_LINE():
    printer = ColoramaPrinter()
    
    assert printer.ADDED_LINE == colorama.Fore.GREEN

def test_ColoramaPrinter_REMOVED_LINE():
    printer = ColoramaPrinter()
    
    assert printer.REMOVED_LINE == colorama.Fore.RED
