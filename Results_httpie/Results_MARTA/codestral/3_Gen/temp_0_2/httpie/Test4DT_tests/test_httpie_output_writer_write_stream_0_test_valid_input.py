
import pytest
from io import StringIO
from unittest.mock import patch
from httpie.output.writer import write_stream

def test_valid_input():
    with patch('sys.stdout', new=StringIO()) as mock_stdout, \
         patch('httpie.output.writer.write_stream') as mock_write_stream:
        f = StringIO('This is a test string.')
        outfile = StringIO()  # Use StringIO for in-memory file handling
        mock_write_stream.return_value = None  # Assuming write_stream returns None if successful

        write_stream(f, outfile, True)

        assert outfile.getvalue() == 'This is a test string.'
