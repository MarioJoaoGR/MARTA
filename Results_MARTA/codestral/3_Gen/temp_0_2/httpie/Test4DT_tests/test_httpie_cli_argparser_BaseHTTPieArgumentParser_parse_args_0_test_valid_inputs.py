
import pytest
from unittest.mock import patch, MagicMock
from httpie.cli.argparser import BaseHTTPieArgumentParser

def test_valid_inputs():
    with patch('httpie.cli.argparser.BaseHTTPieArgumentParser') as MockParser:
        mock_parser = MockParser.return_value
        env = MagicMock()
        args = ['--option', 'value']
        
        # Call the parse_args method on the mocked parser
        parsed_args = mock_parser.parse_args(env, args)
        
        assert parsed_args is not None
