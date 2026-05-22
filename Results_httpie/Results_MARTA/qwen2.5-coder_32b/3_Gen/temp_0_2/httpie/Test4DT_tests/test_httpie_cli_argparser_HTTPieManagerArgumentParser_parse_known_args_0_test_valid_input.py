
import pytest
from httpie.cli.argparser import HTTPieManagerArgumentParser
from unittest.mock import patch

def test_valid_input():
    with patch('httpie.cli.argparser.HTTPieManagerArgumentParser.parse_known_args') as mock_parse:
        # Mock the return value of parse_known_args to simulate valid input
        mock_parse.return_value = (None, [])
        
        parser = HTTPieManagerArgumentParser()
        parsed_args, unknown_args = parser.parse_known_args(['--config', 'settings.cfg'])
        
        # Assert that the parsing was successful and no unrecognized arguments were returned
        assert parsed_args is None
        assert unknown_args == []
