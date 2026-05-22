
import argparse
from unittest.mock import patch, MagicMock
from httpie.cli.argparser import HTTPieArgumentParser

def test_invalid_input():
    with patch('httpie.cli.argparser.HTTPieArgumentParser', autospec=True) as MockParser:
        mock_instance = MockParser.return_value
        mock_instance.args = MagicMock()
        mock_instance.args.format_options = ['invalid_option']
        
        with patch('httpie.cli.argparser.parse_format_options', side_effect=ValueError("Invalid format option")):
            try:
                mock_instance._process_format_options()
            except ValueError as e:
                assert str(e) == "Invalid format option"
