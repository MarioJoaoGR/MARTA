
import sys
from unittest.mock import patch
from httpie.output.writer import write_stream
from io import StringIO

def test_write_stream():
    # Create a mock stream of data
    data = ["line1\n", "line2\n", "line3\n"]
    mock_stream = iter(data)
    
    # Redirect stdout to a buffer for testing
    output_buffer = StringIO()
    
    with patch.object(sys, 'stdout', new=output_buffer):
        write_stream(mock_stream, sys.stdout, True)
        
    assert output_buffer.getvalue() == "".join(data)
