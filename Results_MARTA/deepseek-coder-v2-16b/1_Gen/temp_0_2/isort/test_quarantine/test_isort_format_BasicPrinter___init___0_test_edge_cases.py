
import sys
from io import StringIO
from typing import TextIO

class BasicPrinter:
    ERROR = 'ERROR'
    SUCCESS = 'SUCCESS'
    
    def __init__(self, error: str, success: str, output: TextIO | None = None):
        self.output = output or sys.stdout
        self.success_message = success
        self.error_message = error

    def print_success(self, message: str) -> None:
        """
        Prints a success message to the specified output.
        
        Parameters:
            message (str): The message to be printed when an operation is successful.
        """
        self.output.write(f"SUCCESS: {message}\n")

    def print_error(self, message: str) -> None:
        """
        Prints an error message to the specified output.
        
        Parameters:
            message (str): The message to be printed when an error occurs.
        """
        self.output.write(f"ERROR: {message}\n")
```

Now, let's write a test case that verifies these methods exist and can be called correctly:

```python
import pytest
from io import StringIO
from isort.format import BasicPrinter

@pytest.fixture
def printer():
    return BasicPrinter(error='Error occurred', success='Operation succeeded')

def test_print_success(printer):
    output = StringIO()
    printer.output = output
    message = "The operation was successful!"
    printer.print_success(message)
    assert output.getvalue().strip() == "SUCCESS: The operation was successful!"

def test_print_error(printer):
    output = StringIO()
    printer.output = output
    message = "An error happened."
    printer.print_error(message)
    assert output.getvalue().strip() == "ERROR: An error happened."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_format_BasicPrinter___init___0_test_edge_cases
isort/Test4DT_tests/test_isort_format_BasicPrinter___init___0_test_edge_cases.py:34:9: E0001: Parsing failed: 'unterminated string literal (detected at line 34) (Test4DT_tests.test_isort_format_BasicPrinter___init___0_test_edge_cases, line 34)' (syntax-error)


"""