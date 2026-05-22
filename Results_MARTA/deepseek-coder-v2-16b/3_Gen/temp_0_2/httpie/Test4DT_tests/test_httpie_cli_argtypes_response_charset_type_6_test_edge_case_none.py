
import argparse
from httpie.cli.argtypes import response_charset_type
import unittest.mock as mock

def test_edge_case_none():
    with mock.patch('httpie.cli.argtypes.response_charset_type') as mock_response_charset:
        # Mock the behavior of argparse for testing
        mock_response_charset.side_effect = argparse.ArgumentTypeError("Invalid encoding")
        
        # Call the function with an unsupported encoding
        try:
            response_charset_type('unknown_encoding')
        except argparse.ArgumentTypeError as e:
            assert str(e) == "'unknown_encoding' is not a supported encoding"
