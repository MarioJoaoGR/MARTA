
import pytest
from httpie.context import Environment
import sys
from unittest.mock import patch, MagicMock

def test_valid_inputs():
    with patch('sys.stdin', new=MagicMock()):
        env = Environment(devnull=None)
        assert isinstance(env.stdin, type(sys.stdin))
        assert isinstance(env.stdout, type(sys.stdout))
        assert isinstance(env.stderr, type(sys.stderr))

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_context_Environment_devnull_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        with patch('sys.stdin', new=MagicMock()):
            env = Environment(devnull=None)
>           assert isinstance(env.stdin, type(sys.stdin))
E           assert False
E            +  where False = isinstance(<_pytest.capture.DontReadFromInput object at 0x7f3ff0d22110>, <class 'unittest.mock.MagicMock'>)
E            +    where <_pytest.capture.DontReadFromInput object at 0x7f3ff0d22110> = <Environment {'apply_warnings_filter': <function Environment.apply_warnings_filter at 0x7f3ff07091c0>,\n 'args': Namesp...IO name=6 mode='rb+' closefd=True>" mode='r+' encoding='utf-8'>,\n 'stdout_encoding': 'utf-8',\n 'stdout_isatty': False}>.stdin
E            +    and   <class 'unittest.mock.MagicMock'> = type(<MagicMock id='139912591730832'>)
E            +      where <MagicMock id='139912591730832'> = sys.stdin

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_context_Environment_devnull_0_test_valid_inputs.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_context_Environment_devnull_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.14s ===============================
"""