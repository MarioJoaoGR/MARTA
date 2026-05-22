
import argparse
from httpie.cli.argparser import HTTPieArgumentParser, HTTPieHelpFormatter
from unittest.mock import patch

def test_ensure_one_data_source():
    parser = HTTPieArgumentParser(formatter_class=HTTPieHelpFormatter)
    
    with patch('sys.stdin', new=None):  # Mock stdin to simulate no input from stdin
        try:
            parser._ensure_one_data_source()
        except argparse.ArgumentError as e:
            assert str(e) == 'Request body (from stdin, --raw or a file) and request data (--data or --files) cannot be provided simultaneously.'
