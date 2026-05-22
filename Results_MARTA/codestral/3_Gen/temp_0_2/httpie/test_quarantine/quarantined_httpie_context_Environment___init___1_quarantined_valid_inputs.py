
import pytest
from unittest.mock import patch
from httpie.context import Environment

def test_environment_initialization():
    with patch('sys.stdin', create=True) as mock_stdin:
        mock_stdin.isatty = lambda: True
        env = Environment()
        assert env.stdin_isatty is True

def test_environment_devnull():
    with patch('sys.stdout', create=True) as mock_stdout, \
         patch('sys.stderr', create=True) as mock_stderr:
        mock_stdout.isatty = lambda: True
        mock_stderr.isatty = lambda: True
        env = Environment(devnull=None)
        assert isinstance(env._devnull, type(None))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

httpie/Test4DT_tests_codestral/test_httpie_context_Environment___init___1_test_valid_inputs.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
_______________________ test_environment_initialization ________________________

    def test_environment_initialization():
        with patch('sys.stdin', create=True) as mock_stdin:
            mock_stdin.isatty = lambda: True
            env = Environment()
>           assert env.stdin_isatty is True
E           assert False is True
E            +  where False = <Environment {'apply_warnings_filter': <function Environment.apply_warnings_filter at 0x7f84bb0496c0>,\n 'args': Namesp...IO name=6 mode='rb+' closefd=True>" mode='r+' encoding='utf-8'>,\n 'stdout_encoding': 'utf-8',\n 'stdout_isatty': False}>.stdin_isatty

httpie/Test4DT_tests_codestral/test_httpie_context_Environment___init___1_test_valid_inputs.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_context_Environment___init___1_test_valid_inputs.py::test_environment_initialization
========================= 1 failed, 1 passed in 0.16s ==========================
"""