
import sys
from io import StringIO, TextIOBase
from typing import Optional
import pytest

class BasicPrinter:
    """
    A simple class intended for printing messages to a specified output stream without supporting colored output.

    This class provides basic functionality to direct print statements to either the default standard output (sys.stdout)
    or any other TextIO object, such as a file. It includes predefined constants for error and success statuses which can
    be used in conjunction with message outputs.

    Attributes:
        ERROR (str): A constant string representing an error status.
        SUCCESS (str): A constant string representing a success status.

    Parameters:
        output (Optional[TextIO]): The output stream where the messages will be printed. Defaults to sys.stdout if not provided.
            If a different TextIO object is passed, messages will be directed to that stream instead.

    Methods:
        __init__(self, output: Optional[TextIO] = None):
            Initializes the BasicPrinter with the specified output stream.
    """
    ERROR = 'ERROR'
    SUCCESS = 'SUCCESS'

    def __init__(self, output: Optional[TextIOBase] = None):
        self.output = output or sys.stdout

def test_basic_printer_default_output():
    printer = BasicPrinter()
    assert printer.output == sys.stdout

def test_basic_printer_custom_output():
    custom_output = StringIO()
    printer = BasicPrinter(custom_output)
    assert printer.output == custom_output

def test_basic_printer_write_to_default_output(capsys):
    printer = BasicPrinter()
    message = "This is a test message.\n"
    printer.output.write(message)
    captured = capsys.readouterr()
    assert captured.out == message

def test_basic_printer_write_to_custom_output():
    custom_output = StringIO()
    printer = BasicPrinter(custom_output)
    message = "This is a test message.\n"
    printer.output.write(message)
    assert custom_output.getvalue() == message
