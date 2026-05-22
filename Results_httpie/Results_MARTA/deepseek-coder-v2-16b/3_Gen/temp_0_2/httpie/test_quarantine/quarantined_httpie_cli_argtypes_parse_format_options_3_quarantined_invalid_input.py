
import pytest
from httpie.cli.argtypes import parse_format_options
from unittest.mock import patch
import argparse

def test_invalid_input():
    with patch('httpie.cli.argtypes.argparse', autospec=True):
        s = 'json.indent:2,json.sort_keys:false'
        defaults = {'json': {'indent': 4, 'sort_keys': True}}
    
        try:
            result = parse_format_options(s, defaults)
        except argparse.ArgumentTypeError as e:
            assert str(e) == "invalid value 'false' in 'json.sort_keys:false' (expected <class 'bool'> got <class 'str'>)"
        else:
            raise AssertionError("Expected an ArgumentTypeError but did not get one.")

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argtypes_parse_format_options_3_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with patch('httpie.cli.argtypes.argparse', autospec=True):
            s = 'json.indent:2,json.sort_keys:false'
            defaults = {'json': {'indent': 4, 'sort_keys': True}}
    
            try:
                result = parse_format_options(s, defaults)
            except argparse.ArgumentTypeError as e:
                assert str(e) == "invalid value 'false' in 'json.sort_keys:false' (expected <class 'bool'> got <class 'str'>)"
            else:
>               raise AssertionError("Expected an ArgumentTypeError but did not get one.")
E               AssertionError: Expected an ArgumentTypeError but did not get one.

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argtypes_parse_format_options_3_test_invalid_input.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argtypes_parse_format_options_3_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.24s ===============================
"""