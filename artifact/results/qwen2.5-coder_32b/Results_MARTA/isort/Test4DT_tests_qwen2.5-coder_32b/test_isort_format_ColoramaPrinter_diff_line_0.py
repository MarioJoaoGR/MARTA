
import pytest
from io import StringIO
import colorama
from isort.format import ColoramaPrinter

# Assuming ADDED_LINE_PATTERN and REMOVED_LINE_PATTERN are defined somewhere in your codebase.
# For the sake of this example, let's define them here.
ADDED_LINE_PATTERN = r'^\+[^+]'
REMOVED_LINE_PATTERN = r'^-[^-]'

def test_none_input():
    output_stream = StringIO()
    printer_with_custom_output = ColoramaPrinter(output=output_stream)
    with pytest.raises(TypeError, match="expected string or bytes-like object"):
        printer_with_custom_output.diff_line(None)

def test_added_line():
    output_stream = StringIO()
    printer_with_custom_output = ColoramaPrinter(output=output_stream)
    printer_with_custom_output.diff_line('+ New line')
    assert output_stream.getvalue().strip() == f"{colorama.Fore.GREEN}+ New line{colorama.Style.RESET_ALL}"

def test_removed_line():
    output_stream = StringIO()
    printer_with_custom_output = ColoramaPrinter(output=output_stream)
    printer_with_custom_output.diff_line('- Old line')
    assert output_stream.getvalue().strip() == f"{colorama.Fore.RED}- Old line{colorama.Style.RESET_ALL}"

def test_no_change_line():
    output_stream = StringIO()
    printer_with_custom_output = ColoramaPrinter(output=output_stream)
    printer_with_custom_output.diff_line('Unchanged line')
    assert output_stream.getvalue().strip() == "Unchanged line"

def test_error_message():
    printer = ColoramaPrinter()
    assert printer.ERROR == f"{colorama.Fore.RED}ERROR{colorama.Style.RESET_ALL}"

def test_success_message():
    printer = ColoramaPrinter()
    assert printer.SUCCESS == f"{colorama.Fore.GREEN}SUCCESS{colorama.Style.RESET_ALL}"
