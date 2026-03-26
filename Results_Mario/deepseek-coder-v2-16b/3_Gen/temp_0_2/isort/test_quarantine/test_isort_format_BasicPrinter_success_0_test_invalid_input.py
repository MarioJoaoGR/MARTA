
import pytest
from io import StringIO
from unittest.mock import patch

class BasicPrinter:
    ERROR = 'ERROR'
    SUCCESS = 'SUCCESS'
    
    def __init__(self, error: str, success: str, output: TextIO | None = None):
        self.output = output or sys.stdout
        self.success_message = success
        self.error_message = error

    def success(self, message: str) -> None:
        print(self.success_message.format(success=self.SUCCESS, message=message), file=self.output)

def test_invalid_input():
    with patch('sys.stdout', new=StringIO()) as mock_stdout:
        printer = BasicPrinter(error='An error occurred', success='Operation successful')
        with pytest.raises(TypeError):
            printer.success(123)  # Providing a non-string value should raise a TypeError
        
        assert "ERROR" not in mock_stdout.getvalue()  # Ensure no ERROR message is printed
        assert "Operation successful" not in mock_stdout.getvalue()  # Ensure no success message is printed

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_format_BasicPrinter_success_0_test_invalid_input
isort/Test4DT_tests/test_isort_format_BasicPrinter_success_0_test_invalid_input.py:10:57: E0602: Undefined variable 'TextIO' (undefined-variable)
isort/Test4DT_tests/test_isort_format_BasicPrinter_success_0_test_invalid_input.py:11:32: E0602: Undefined variable 'sys' (undefined-variable)


"""