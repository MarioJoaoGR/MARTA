
import colorama
from io import StringIO
import pytest

# Assuming ColoramaPrinter is part of a module named 'isort.format'
from isort.format import ColoramaPrinter

def setup_module(module):
    # Initialize colorama for tests
    colorama.init(autoreset=True)

def teardown_module(module):
    # Deinitialize colorama after tests
    colorama.deinit()

def test_ColoramaPrinter_init_default_output():
    printer = ColoramaPrinter()
    assert printer.ERROR == f"{colorama.Fore.RED}ERROR{colorama.Style.RESET_ALL}"
    assert printer.SUCCESS == f"{colorama.Fore.GREEN}SUCCESS{colorama.Style.RESET_ALL}"

def test_ColoramaPrinter_init_custom_output():
    output_stream = StringIO()
    printer = ColoramaPrinter(output=output_stream)
    assert printer.ERROR == f"{colorama.Fore.RED}ERROR{colorama.Style.RESET_ALL}"
    assert printer.SUCCESS == f"{colorama.Fore.GREEN}SUCCESS{colorama.Style.RESET_ALL}"

def test_ColoramaPrinter_style_text_with_style():
    printer = ColoramaPrinter()
    styled_text = printer.style_text("Hello, World!", colorama.Fore.BLUE)
    expected_output = f"{colorama.Fore.BLUE}Hello, World!{colorama.Style.RESET_ALL}"
    assert styled_text == expected_output

def test_ColoramaPrinter_style_text_without_style():
    printer = ColoramaPrinter()
    styled_text = printer.style_text("Hello, World!")
    expected_output = "Hello, World!"
    assert styled_text == expected_output
