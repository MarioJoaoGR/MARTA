
import sys
from io import StringIO
import pytest
from isort.format import BasicPrinter

def test_basic_printer_default_output():
    # Capture stdout to check the output of the printer
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Create an instance of BasicPrinter with default output (sys.stdout)
    printer = BasicPrinter()
    
    # Write a success message using the output attribute
    printer.output.write(f"{BasicPrinter.SUCCESS}: Operation completed successfully.\n")
    
    # Reset stdout to its original value
    sys.stdout = sys.__stdout__
    
    # Assert that the correct message was written to stdout
    assert captured_output.getvalue() == f"{BasicPrinter.SUCCESS}: Operation completed successfully.\n"

def test_basic_printer_custom_output():
    # Create a custom TextIO object (StringIO in this case)
    custom_output = StringIO()
    
    # Create an instance of BasicPrinter with the custom output
    printer = BasicPrinter(custom_output)
    
    # Write a success message using the output attribute
    printer.output.write(f"{BasicPrinter.SUCCESS}: This message will be written to custom output.\n")
    
    # Assert that the correct message was written to the custom output
    assert custom_output.getvalue() == f"{BasicPrinter.SUCCESS}: This message will be written to custom output.\n"

def test_basic_printer_error_method():
    # Capture stderr to check the error output of the printer
    captured_stderr = StringIO()
    sys.stderr = captured_stderr
    
    # Create an instance of BasicPrinter with default output (sys.stdout)
    printer = BasicPrinter()
    
    # Call the error method to print an error message
    printer.error("An error occurred during processing.")
    
    # Reset stderr to its original value
    sys.stderr = sys.__stderr__
    
    # Assert that the correct error message was written to stderr
    assert captured_stderr.getvalue() == f"{BasicPrinter.ERROR}: An error occurred during processing.\n"
