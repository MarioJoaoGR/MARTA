
# Function Code
class BasicPrinter:
    ERROR = 'ERROR'
    SUCCESS = 'SUCCESS'
    
    def __init__(self, error: str, success: str, output: TextIO | None = None):
        if not isinstance(error, str) or not isinstance(success, str):
            raise TypeError("Both 'error' and 'success' must be strings.")
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

```python
# Test Case Code
import pytest
from isort.format import BasicPrinter
import sys

def test_invalid_input():
    with pytest.raises(TypeError):
        BasicPrinter("Error template", 123)

def test_invalid_type_error_message():
    with pytest.raises(TypeError):
        BasicPrinter(123, "Success template")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_format_BasicPrinter_success_0_test_invalid_input
isort/Test4DT_tests/test_isort_format_BasicPrinter_success_0_test_invalid_input.py:37:1: E0001: Parsing failed: 'invalid syntax (Test4DT_tests.test_isort_format_BasicPrinter_success_0_test_invalid_input, line 37)' (syntax-error)


"""