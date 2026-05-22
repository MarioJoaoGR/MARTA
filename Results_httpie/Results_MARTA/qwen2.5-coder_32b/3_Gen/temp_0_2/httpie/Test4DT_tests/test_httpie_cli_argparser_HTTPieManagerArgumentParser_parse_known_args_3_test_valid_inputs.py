
import pytest
from httpie.cli.argparser import HTTPieManagerArgumentParser
from unittest.mock import patch

def test_valid_inputs():
    with patch('httpie.cli.argparser.HTTPieManagerArgumentParser.parse_known_args', return_value=([], [])):
        parser = HTTPieManagerArgumentParser()
        parsed_args, unknown_args = parser.parse_known_args(['--config', 'settings.cfg'])
        assert isinstance(parsed_args, list)
        assert isinstance(unknown_args, list)
