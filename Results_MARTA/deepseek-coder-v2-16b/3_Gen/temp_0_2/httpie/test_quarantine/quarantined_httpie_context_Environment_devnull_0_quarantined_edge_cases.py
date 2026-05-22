
import pytest
from unittest.mock import patch, MagicMock
import sys
import os
from httpie.context import Environment

@pytest.fixture
def environment():
    return Environment()

def test_environment_devnull(environment):
    with patch('sys.stderr', new=MagicMock()) as mock_stderr:
        assert environment.stderr == sys.stderr

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_context_Environment_devnull_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
___________________________ test_environment_devnull ___________________________

environment = <Environment {'apply_warnings_filter': <function Environment.apply_warnings_filter at 0x7f6ff6ec2480>,
 'args': Namesp...IO name=6 mode='rb+' closefd=True>" mode='r+' encoding='utf-8'>,
 'stdout_encoding': 'utf-8',
 'stdout_isatty': False}>

    def test_environment_devnull(environment):
        with patch('sys.stderr', new=MagicMock()) as mock_stderr:
>           assert environment.stderr == sys.stderr
E           AssertionError: assert <_io.TextIOWr...oding='utf-8'> == <MagicMock id...118860786320'>
E             
E             Use -v to get more diff

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_context_Environment_devnull_0_test_edge_cases.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_context_Environment_devnull_0_test_edge_cases.py::test_environment_devnull
============================== 1 failed in 0.12s ===============================
"""