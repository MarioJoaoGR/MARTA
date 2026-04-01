
import sys
from io import StringIO
from unittest.mock import patch
from isort.format import BasicPrinter  # Correctly importing from isort.format

def test_diff_line():
    # Prepare a sample line to be written
    sample_line = "This is a sample line."
    
    # Create a mock output (StringIO allows us to capture the output)
    output = StringIO()
    
    # Instantiate the BasicPrinter with the mock output
    printer = BasicPrinter(error='ERROR', success='SUCCESS', output=output)
    
    # Call the method under test
    printer.diff_line(sample_line)
    
    # Get the content of the mock output
    result = output.getvalue().strip()
    
    # Assert that the written line matches the sample line
    assert result == sample_line, f"Expected '{sample_line}', but got '{result}'"
