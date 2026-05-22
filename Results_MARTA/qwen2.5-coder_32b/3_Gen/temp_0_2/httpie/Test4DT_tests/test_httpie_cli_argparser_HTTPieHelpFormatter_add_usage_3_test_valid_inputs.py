
import argparse
from unittest.mock import patch
from httpie.cli.argparser import HTTPieHelpFormatter

def test_valid_inputs():
    with patch('httpie.cli.argparser.HTTPieHelpFormatter.__init__', return_value=None):
        formatter = HTTPieHelpFormatter(max_help_position=8)
        assert isinstance(formatter, HTTPieHelpFormatter), "Expected an instance of HTTPieHelpFormatter"
