
import sys
from io import TextIOBase
from unittest.mock import patch

from isort.format import BasicPrinter


def test_diff_line():
    # Create a mock for the output
    class MockOutput(TextIOBase):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.written = []
        
        def write(self, s: str):
            self.written.append(s)
            return len(s)
    
    # Create an instance of BasicPrinter with the mock output
    error_msg = "An error occurred"
    success_msg = "Operation successful"
    mock_output = MockOutput()
    printer = BasicPrinter(error=error_msg, success=success_msg, output=mock_output)
    
    # Define a sample line to be written
    sample_line = "This is a sample line."
    
    # Call the method under test
    with patch.object(sys.stdout, 'write') as mock_write:
        printer.diff_line(sample_line)
        
        # Check if the write method was called with the correct argument
        assert len(mock_output.written) == 1
        assert mock_output.written[0] == sample_line
