
import argparse
from httpie.client import make_send_kwargs
import unittest.mock as mock

def test_valid_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('--timeout', type=float, help='Timeout for the request in seconds.')
    args = parser.parse_args(['--timeout', '5.0'])
    
    with mock.patch('httpie.client.make_send_kwargs') as mock_make_send_kwargs:
        result = make_send_kwargs(args)
        assert result == {'timeout': 5.0, 'allow_redirects': False}
