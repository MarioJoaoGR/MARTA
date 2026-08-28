
import pytest
from io import StringIO
import sys
from isort.format import BasicPrinter

def test_print_error_message():
    bp = BasicPrinter()
    captured_stderr = StringIO()
    original_stderr = sys.stderr
    sys.stderr = captured_stderr
    
    message = "An error occurred: Unable to connect to database."
    status = "ERROR"
    bp.error(message)
    
    sys.stderr = original_stderr
    assert captured_stderr.getvalue().strip() == f"{BasicPrinter.ERROR}: {message}"


def test_invalid_input():
    bp = BasicPrinter()
    captured_stderr = StringIO()
    original_stderr = sys.stderr
    sys.stderr = captured_stderr
    
    with pytest.raises(NameError):
        print_message("Invalid input", "INVALID")  # Assuming print_message is defined elsewhere in the module
    
    sys.stderr = original_stderr