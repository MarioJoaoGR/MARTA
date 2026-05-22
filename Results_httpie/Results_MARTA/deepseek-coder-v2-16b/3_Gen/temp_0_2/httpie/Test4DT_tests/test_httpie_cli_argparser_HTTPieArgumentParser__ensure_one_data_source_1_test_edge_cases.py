
import argparse
from httpie.cli.argparser import HTTPieArgumentParser, HTTPieHelpFormatter
from unittest.mock import patch

def test_ensure_one_data_source():
    parser = HTTPieArgumentParser(formatter_class=HTTPieHelpFormatter)
    
    with patch('sys.stdin', new_callable=lambda: None):  # Mock stdin if needed
        try:
            parser._ensure_one_data_source()
        except SystemExit as e:
            assert str(e) == 'Request body (from stdin, --raw or a file) and request data (--data or --files) cannot be provided simultaneously.'
