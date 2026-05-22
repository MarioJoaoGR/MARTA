
import sys
from unittest.mock import patch
import requests
from httpie.client import dump_request

def test_none_input():
    with patch('sys.stderr') as mock_stderr:
        kwargs = {}
        dump_request(kwargs)
        expected_output = f'\n>>> requests.request(**{repr(kwargs)})\n\n'
        mock_stderr.write.assert_called_with(expected_output)
