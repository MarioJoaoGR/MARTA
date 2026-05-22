
import argparse
from unittest.mock import patch, MagicMock
from httpie.cli.argparser import HTTPieArgumentParser

def test_valid_case():
    with patch('httpie.cli.argparser.HTTPieArgumentParser.__init__', return_value=None):
        parser = HTTPieArgumentParser()
        mock_args = argparse.Namespace(some_argument='value')
        with patch.object(parser, 'print_usage', lambda file: None):
            parser.print_usage(file=MagicMock())
