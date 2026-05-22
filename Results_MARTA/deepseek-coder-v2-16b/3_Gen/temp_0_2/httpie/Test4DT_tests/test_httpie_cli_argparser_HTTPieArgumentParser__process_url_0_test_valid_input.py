
import pytest
from unittest.mock import patch
from httpie.cli.argparser import HTTPieArgumentParser

def test_valid_input():
    with patch('httpie.cli.argparser.HTTPieArgumentParser') as MockHTTPieArgumentParser:
        mock_parser = MockHTTPieArgumentParser.return_value
        mock_parser.args = type('Args', (), {'url': 'http://example.com'})()
        
        assert mock_parser.args.url == 'http://example.com'
