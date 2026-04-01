
import pytest
from unittest.mock import MagicMock
from isort.format import BasicPrinter  # Assuming this is the correct module path

@pytest.fixture
def printer():
    return BasicPrinter(error='Error occurred', success='Operation succeeded')

def test_diff_line(printer):
    mock_output = MagicMock()
    printer.output = mock_output
    
    line = "This is a log message."
    printer.diff_line(line)
    
    assert mock_output.write.call_count == 1
    mock_output.write.assert_called_with("This is a log message.")
