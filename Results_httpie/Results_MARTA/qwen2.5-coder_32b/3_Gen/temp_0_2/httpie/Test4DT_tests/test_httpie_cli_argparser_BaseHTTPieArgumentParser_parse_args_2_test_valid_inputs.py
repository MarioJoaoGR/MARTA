
import pytest
from unittest.mock import MagicMock, patch
from httpie.cli.argparser import BaseHTTPieArgumentParser
from argparse import Namespace

def test_valid_inputs():
    parser = BaseHTTPieArgumentParser()
    
    # Mock an Environment object
    env_mock = MagicMock()
    env_mock.stdin = True
    env_mock.stdin_isatty = False
    
    with patch('httpie.cli.argparser.BaseHTTPieArgumentParser.parse_known_args', return_value=(Namespace(debug=False), [])):
        # Call the parse_args method with the mocked environment
        parsed_args = parser.parse_args(env=env_mock, args=['--option', 'value'])
        
        assert isinstance(parsed_args, Namespace)
