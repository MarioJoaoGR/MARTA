
import pytest
from unittest.mock import patch, MagicMock
from httpie.cli.argparser import HTTPieArgumentParser
from httpie.output.ui import rich_help
from io import StringIO
import sys

@pytest.fixture
def parser():
    return HTTPieArgumentParser(formatter_class=HTTPieHelpFormatter)

def test_print_usage(parser):
    with patch('httpie.cli.argparser.sys.exc_info', return_value=(None, None, None)):
        # Redirect stdout to a string buffer for testing purposes
        output = StringIO()
        parser.env.rich_error_console = MagicMock(spec=StringIO)
        
        # Call the method under test
        parser.print_usage(file=output)
        
        # Assert that the usage information was printed correctly
        expected_usage = rich_help.to_usage(parser.spec, whitelist=set())
        parser.env.rich_error_console.print.assert_called_with(expected_usage)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_cli_argparser_HTTPieArgumentParser_print_usage_2_test_edge_cases
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argparser_HTTPieArgumentParser_print_usage_2_test_edge_cases.py:11:48: E0602: Undefined variable 'HTTPieHelpFormatter' (undefined-variable)


"""