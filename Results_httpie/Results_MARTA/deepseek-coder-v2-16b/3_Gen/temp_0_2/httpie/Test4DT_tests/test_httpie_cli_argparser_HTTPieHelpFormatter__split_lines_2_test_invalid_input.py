
import pytest
from unittest.mock import patch
from httpie.cli.argparser import HTTPieHelpFormatter

def test_invalid_input():
    with patch('httpie.cli.argparser.HTTPieHelpFormatter.__init__', return_value=None):
        instance = HTTPieHelpFormatter(max_help_position='not an integer')
        assert isinstance(instance, HTTPieHelpFormatter)
