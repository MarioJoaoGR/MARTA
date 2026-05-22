
import pytest
import argparse
from typing import List

def _parse_options(args: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('task_id')
    parser.add_argument('--daemon', action='store_true')
    return parser.parse_known_args(args)[0]

def test_invalid_input():
    with pytest.raises(SystemExit):
        _parse_options([1234])  # Invalid input type, should raise SystemExit

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_internal_daemon_runner__parse_options_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(SystemExit):
>           _parse_options([1234])  # Invalid input type, should raise SystemExit

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_internal_daemon_runner__parse_options_1_test_invalid_input.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_internal_daemon_runner__parse_options_1_test_invalid_input.py:10: in _parse_options
    return parser.parse_known_args(args)[0]
/usr/local/lib/python3.11/argparse.py:1907: in parse_known_args
    namespace, args = self._parse_known_args(args, namespace)
/usr/local/lib/python3.11/argparse.py:1950: in _parse_known_args
    option_tuple = self._parse_optional(arg_string)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = ArgumentParser(prog='__main__.py', usage=None, description=None, formatter_class=<class 'argparse.HelpFormatter'>, conflict_handler='error', add_help=True)
arg_string = 1234

    def _parse_optional(self, arg_string):
        # if it's an empty string, it was meant to be a positional
        if not arg_string:
            return None
    
        # if it doesn't start with a prefix, it was meant to be positional
>       if not arg_string[0] in self.prefix_chars:
E       TypeError: 'int' object is not subscriptable

/usr/local/lib/python3.11/argparse.py:2249: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_internal_daemon_runner__parse_options_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.13s ===============================
"""