
import argparse
from httpie.cli.argparser import HTTPieArgumentParser, HTTPieHelpFormatter
import unittest
from unittest.mock import patch

class TestHTTPieArgumentParserInit(unittest.TestCase):
    @patch('httpie.cli.argparser.argparse.ArgumentParser')
    def test_init(self, mock_argparse):
        # Arrange
        formatter = HTTPieHelpFormatter()
        
        # Act
        parser = HTTPieArgumentParser(formatter_class=formatter)
        
        # Assert
        mock_argparse.assert_called_with(formatter_class=formatter)

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argparser_HTTPieArgumentParser___init___0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
____________________ TestHTTPieArgumentParserInit.test_init ____________________

self = <test_httpie_cli_argparser_HTTPieArgumentParser___init___0_test_edge_cases.TestHTTPieArgumentParserInit testMethod=test_init>
mock_argparse = <MagicMock name='ArgumentParser' id='140375238006608'>

    @patch('httpie.cli.argparser.argparse.ArgumentParser')
    def test_init(self, mock_argparse):
        # Arrange
>       formatter = HTTPieHelpFormatter()

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argparser_HTTPieArgumentParser___init___0_test_edge_cases.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.cli.argparser.HTTPieHelpFormatter object at 0x7faba831bf10>
max_help_position = 6, args = (), kwargs = {'max_help_position': 6}

    def __init__(self, max_help_position=6, *args, **kwargs):
        # A smaller indent for args help.
        kwargs['max_help_position'] = max_help_position
>       super().__init__(*args, **kwargs)
E       TypeError: HelpFormatter.__init__() missing 1 required positional argument: 'prog'

httpie/httpie/cli/argparser.py:45: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argparser_HTTPieArgumentParser___init___0_test_edge_cases.py::TestHTTPieArgumentParserInit::test_init
============================== 1 failed in 0.22s ===============================
"""