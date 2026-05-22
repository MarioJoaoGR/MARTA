
import unittest
from httpie.cli.argparser import HTTPieHelpFormatter
from textwrap import dedent

class TestHTTPieHelpFormatter(unittest.TestCase):
    def test_valid_input(self):
        formatter = HTTPieHelpFormatter(max_help_position=8)
        text = """
        Usage: http [OPTIONS] URL
        
        Options:
          --version             Show version and exit.
          -h, --help            Show help.
          -v, --verbose         Make the operation more talkative.
          -a VALUE               Add custom header VALUE.
          --auth AUTH           HTTP basic authentication.
          --body-file FILE      Read body from FILE.
        """
        expected_lines = [
            "Usage: http [OPTIONS] URL",
            "",
            "Options:",
            "  --version             Show version and exit.",
            "  -h, --help            Show help.",
            "  -v, --verbose         Make the operation more talkative.",
            "  -a VALUE               Add custom header VALUE.",
            "  --auth AUTH           HTTP basic authentication.",
            "  --body-file FILE      Read body from FILE."
        ]
        with self.subTest():
            lines = formatter._split_lines(text, width=80)
            self.assertEqual(lines, expected_lines)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argparser_HTTPieHelpFormatter__split_lines_5_test_valid_input.py F [100%]

=================================== FAILURES ===================================
___________________ TestHTTPieHelpFormatter.test_valid_input ___________________

self = <test_httpie_cli_argparser_HTTPieHelpFormatter__split_lines_5_test_valid_input.TestHTTPieHelpFormatter testMethod=test_valid_input>

    def test_valid_input(self):
>       formatter = HTTPieHelpFormatter(max_help_position=8)

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argparser_HTTPieHelpFormatter__split_lines_5_test_valid_input.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.cli.argparser.HTTPieHelpFormatter object at 0x7fdc33807950>
max_help_position = 8, args = (), kwargs = {'max_help_position': 8}

    def __init__(self, max_help_position=6, *args, **kwargs):
        # A smaller indent for args help.
        kwargs['max_help_position'] = max_help_position
>       super().__init__(*args, **kwargs)
E       TypeError: HelpFormatter.__init__() missing 1 required positional argument: 'prog'

httpie/httpie/cli/argparser.py:45: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argparser_HTTPieHelpFormatter__split_lines_5_test_valid_input.py::TestHTTPieHelpFormatter::test_valid_input
============================== 1 failed in 0.28s ===============================
"""