
import pytest
from isort.format import BasicPrinter

def test_basicprinter_success():
    """Test that a success message is printed correctly."""
    from io import StringIO
    output = StringIO()
    printer = BasicPrinter(output)
    printer.success("Operation completed successfully.")
    assert "SUCCESS: Operation completed successfully." in output.getvalue().strip()

def test_basicprinter_error():
    """Test that an error message is printed correctly."""
    from io import StringIO
    output = StringIO()
    printer = BasicPrinter(output)
    printer.success("An error occurred: Unable to connect to database.")
    assert "SUCCESS: An error occurred: Unable to connect to database." in output.getvalue().strip()
