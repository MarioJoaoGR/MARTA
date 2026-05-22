
import argparse
from unittest.mock import patch, MagicMock
import pytest
from httpie_argument_parser import HTTPieArgumentParser, HTTPieHelpFormatter

@pytest.fixture
def parser():
    return HTTPieArgumentParser(formatter_class=HTTPieHelpFormatter)

def test_print_manual_with_available_man_page(parser):
    # Mock the man_pages module to simulate a successful check for available man pages
    with patch('httpie.output.ui.man_pages') as mock_man_pages:
        mock_man_pages.is_available.return_value = True
        mock_man_pages.display_for = MagicMock()  # Mock the display_for method
        
        parser.env.program_name = 'httpie'  # Set a program name for the environment
        parser.print_manual()
        
        mock_man_pages.is_available.assert_called_once_with('httpie')
        mock_man_pages.display_for.assert_called_once_with(parser.env, 'httpie')

def test_print_manual_without_available_man_page(parser):
    # Mock the man_pages module to simulate a failed check for available man pages
    with patch('httpie.output.ui.man_pages') as mock_man_pages:
        mock_man_pages.is_available.return_value = False
        
        parser.env.program_name = 'httpie'  # Set a program name for the environment
        with patch('httpie_argument_parser.HTTPieArgumentParser.format_help', return_value='Manual content'):
            parser.print_manual()
            
            mock_man_pages.is_available.assert_called_once_with('httpie')
            assert 'Manual content' in parser.env.rich_console.pager().__enter__().text  # Check if the help text is printed

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_cli_argparser_HTTPieArgumentParser_print_manual_0_test_valid_inputs
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argparser_HTTPieArgumentParser_print_manual_0_test_valid_inputs.py:5:0: E0401: Unable to import 'httpie_argument_parser' (import-error)


"""