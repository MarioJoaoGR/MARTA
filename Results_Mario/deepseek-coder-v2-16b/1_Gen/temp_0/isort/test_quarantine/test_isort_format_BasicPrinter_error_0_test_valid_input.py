
import sys
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
            
        Returns:
            None
        """
        self.output.write(f"{self.success_message}: {message}\n")
        
    def print_error(self, message: str) -> None:
        """
        Prints an error message to the specified output.
        
        Parameters:
            message (str): The message to be printed when an error occurs.
            
        Returns:
            None
        """
        self.output.write(f"{self.error_message}: {message}\n")
```

Now, let's write the test case to ensure that these methods are correctly implemented and can be used in the tests:

```python
import pytest
from isort.format import BasicPrinter

@pytest.fixture
def printer():
    return BasicPrinter(error="ERROR", success="SUCCESS")

def test_print_success(capsys, printer):
    printer.print_success("Hello, world!")
    captured = capsys.readouterr()
    assert "SUCCESS: Hello, world!" in captured.out

def test_print_error(capsys, printer):
    printer.print_error("Something went wrong.")
    captured = capsys.readouterr()
    assert "ERROR: Something went wrong." in captured.out

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_format_BasicPrinter_error_0_test_valid_input
isort/Test4DT_tests/test_isort_format_BasicPrinter_error_0_test_valid_input.py:39:9: E0001: Parsing failed: 'unterminated string literal (detected at line 39) (Test4DT_tests.test_isort_format_BasicPrinter_error_0_test_valid_input, line 39)' (syntax-error)


"""