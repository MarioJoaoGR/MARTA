
import pytest
from unittest.mock import patch
from httpie.cli.argparser import HTTPieArgumentParser

def test_error_case():
    with patch('httpie.output.ui.man_pages.is_available', return_value=False):
        parser = HTTPieArgumentParser()
        with patch('httpie.cli.argparser.HTTPieArgumentParser.format_help', return_value="Manual content"):
            assert parser.print_manual() is None

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

httpie/Test4DT_tests_codestral/test_httpie_cli_argparser_HTTPieArgumentParser_print_manual_0_test_error_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_error_case ________________________________

    def test_error_case():
        with patch('httpie.output.ui.man_pages.is_available', return_value=False):
            parser = HTTPieArgumentParser()
            with patch('httpie.cli.argparser.HTTPieArgumentParser.format_help', return_value="Manual content"):
>               assert parser.print_manual() is None

httpie/Test4DT_tests_codestral/test_httpie_cli_argparser_HTTPieArgumentParser_print_manual_0_test_error_case.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = HTTPieArgumentParser(prog='__main__.py', usage=None, description=None, formatter_class=<class 'httpie.cli.argparser.HTTPieHelpFormatter'>, conflict_handler='error', add_help=False)

    def print_manual(self):
        from httpie.output.ui import man_pages
    
>       if man_pages.is_available(self.env.program_name):
E       AttributeError: 'NoneType' object has no attribute 'program_name'

httpie/httpie/cli/argparser.py:564: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_cli_argparser_HTTPieArgumentParser_print_manual_0_test_error_case.py::test_error_case
============================== 1 failed in 0.27s ===============================
"""