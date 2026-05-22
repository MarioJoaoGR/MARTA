
import argparse
from unittest import TestCase, mock
from httpie.cli.argparser import HTTPieArgumentParser
from httpie.output.ui import man_pages

class TestHTTPieArgumentParserPrintManual(TestCase):
    @mock.patch('httpie.cli.argparser.HTTPieArgumentParser.format_help')
    def test_print_manual_with_man_pages(self, mock_format_help):
        # Mock the man pages to be available
        with mock.patch('httpie.output.ui.man_pages.is_available', return_value=True):
            parser = HTTPieArgumentParser()
            parser.env = mock.Mock(program_name='httpie')
            
            # Call the method under test
            parser.print_manual()
            
            # Assert that man_pages.display_for was called with the correct arguments
            man_pages.display_for.assert_called_once_with(parser.env, 'httpie')
    
    @mock.patch('httpie.cli.argparser.HTTPieArgumentParser.format_help')
    def test_print_manual_without_man_pages(self, mock_format_help):
        # Mock the man pages to be unavailable
        with mock.patch('httpie.output.ui.man_pages.is_available', return_value=False):
            parser = HTTPieArgumentParser()
            parser.env = mock.Mock(program_name='httpie')
            
            # Call the method under test
            parser.print_manual()
            
            # Assert that format_help was called
            mock_format_help.assert_called_once()
            
            # Assert that the text is printed using rich console pager
            with mock.patch('httpie.cli.argparser.HTTPieArgumentParser.env.rich_console.pager'):
                parser.env.rich_console.print.assert_called_once_with(mock_format_help.return_value, highlight=False)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_cli_argparser_HTTPieArgumentParser_print_manual_0_test_valid_case
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argparser_HTTPieArgumentParser_print_manual_0_test_valid_case.py:19:12: E1101: Function 'display_for' has no 'assert_called_once_with' member (no-member)


"""