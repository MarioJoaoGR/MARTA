
import pytest
from io import StringIO
from httpie.output.writer import write_stream
from unittest.mock import patch

def test_valid_input():
    with patch('sys.stdout', new=StringIO()) as mock_stdout, \
         patch('httpie.output.writer.open', create=True) as mock_open:
        # Mock the open function to return a StringIO object for 'temp_output.txt'
        mock_file = StringIO()
        mock_open.return_value.__enter__.return_value = mock_file
        
        f = StringIO('This is a test string.')
        outfile = mock_open.return_value.__enter__.return_value
        write_stream(f, outfile, True)
        
        # Assert that the content was written correctly to the mock file
        assert 'This is a test string.' in mock_file.getvalue()
