
import argparse
from unittest import TestCase, mock
from httpie.cli.argparser import HTTPieArgumentParser

class TestHTTPieArgumentParser(TestCase):
    @mock.patch('httpie.output.ui.man_pages')
    def test_print_manual(self, mock_man_pages):
        parser = HTTPieArgumentParser()
        parser.env = mock.Mock()
        parser.env.program_name = 'httpie'
        
        # Mock the is_available method to return True for testing purposes
        mock_man_pages.is_available.return_value = True
        
        # Call the print_manual method
        parser.print_manual()
        
        # Assert that man_pages.display_for was called with the correct arguments
        mock_man_pages.display_for.assert_called_with(parser.env, 'httpie')

    @mock.patch('httpie.output.ui.man_pages')
    def test_print_manual_no_man_page(self, mock_man_pages):
        parser = HTTPieArgumentParser()
        parser.env = mock.Mock()
        parser.env.program_name = 'httpie'
        
        # Mock the is_available method to return False for testing purposes
        mock_man_pages.is_available.return_value = False
        
        # Call the print_manual method and capture stdout
        with mock.patch('sys.stdout', new_callable=mock.StringIO) as mock_stdout:
            parser.print_manual()
            
            # Assert that format_help was called
            self.assertTrue(parser.format_help.called)
            output = mock_stdout.getvalue().strip()
            expected_output = parser.format_help().strip()
            self.assertEqual(output, expected_output)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_cli_argparser_HTTPieArgumentParser_print_manual_1_test_valid_case
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argparser_HTTPieArgumentParser_print_manual_1_test_valid_case.py:32:51: E1101: Module 'unittest.mock' has no 'StringIO' member (no-member)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argparser_HTTPieArgumentParser_print_manual_1_test_valid_case.py:36:28: E1101: Method 'format_help' has no 'called' member (no-member)


"""