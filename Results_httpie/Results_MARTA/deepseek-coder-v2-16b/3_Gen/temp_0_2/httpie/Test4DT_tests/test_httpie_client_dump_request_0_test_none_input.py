
import sys
from io import StringIO
from unittest.mock import patch
import requests
from httpie.client import dump_request

def test_none_input():
    with patch('sys.stderr', new=StringIO()) as mock_stderr:
        # Call the function with no input parameters
        dump_request({})
        
        # Get the output from the mock stderr
        output = mock_stderr.getvalue().strip()
        
        # Check that the output matches the expected string
        assert output == '>>> requests.request(**{})'
