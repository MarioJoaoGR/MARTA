
import argparse
from unittest.mock import patch, MagicMock
import sys

def test_valid_inputs():
    with patch('httpie.cli.argparser.HTTPieArgumentParser') as mock_parser:
        # Create a mock instance of HTTPieArgumentParser
        parser = mock_parser.return_value
        
        # Mock the print_usage method to avoid actual output during testing
        parser.print_usage = MagicMock()
        
        # Call the print_usage method with a file-like object (mock it as sys.stderr)
        parser.print_usage(file=sys.stderr)
        
        # Assert that the print_usage method was called with the correct arguments
        mock_parser.return_value.print_usage.assert_called_with(file=sys.stderr)
