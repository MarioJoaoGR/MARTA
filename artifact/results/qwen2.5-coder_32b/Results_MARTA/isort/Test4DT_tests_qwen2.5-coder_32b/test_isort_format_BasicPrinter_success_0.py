
import sys
from io import StringIO
import pytest

# Assuming BasicPrinter is defined in a module named 'isort.format'
from isort.format import BasicPrinter

def test_success_with_default_output():
    # Capture stdout to check the output of the success method
    captured_output = StringIO()
    sys.stdout = captured_output
    
    printer = BasicPrinter()
    printer.success("Operation completed successfully.")
    
    assert captured_output.getvalue() == "SUCCESS: Operation completed successfully.\n"

def test_success_with_custom_file_output():
    # Create a file object to capture the output of the success method
    with open('test_output.txt', 'w') as custom_file:
        printer = BasicPrinter(custom_file)
        printer.success("This message goes to the file.")
    
    # Read the content from the file to assert the expected output
    with open('test_output.txt', 'r') as custom_file:
        file_content = custom_file.read()
    
    assert file_content == "SUCCESS: This message goes to the file.\n"

def test_success_with_empty_string_message():
    # Capture stdout to check the output of the success method with an empty string
    captured_output = StringIO()
    sys.stdout = captured_output
    
    printer = BasicPrinter()
    printer.success("")
    
    assert captured_output.getvalue() == "SUCCESS: \n"
