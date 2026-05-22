
import pytest
from unittest.mock import patch, MagicMock
from httpie.context import Environment
import sys
from pathlib import Path

@pytest.fixture(scope="function")
def valid_environment():
    with patch('sys.stdin', new=MagicMock()):
        with patch('sys.stdout', new=MagicMock()):
            with patch('sys.stderr', new=MagicMock()):
                env = Environment(config_dir='/tmp/config', program_name='test_program')
    return env

def test_valid_inputs(valid_environment):
    assert valid_environment.config_dir == Path('/tmp/config')
    assert valid_environment.program_name == 'test_program'
    assert valid_environment.stdin is not None
    assert valid_environment.stdout is not None
    assert valid_environment.stderr is not None
    assert valid_environment.colors == 256
    assert valid_environment.show_displays is True

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_context_Environment___init___0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

valid_environment = <Environment {'apply_warnings_filter': <function Environment.apply_warnings_filter at 0x7f340e12e2a0>,
 'args': Namesp...IO name=6 mode='rb+' closefd=True>" mode='r+' encoding='utf-8'>,
 'stdout_encoding': 'utf-8',
 'stdout_isatty': False}>

    def test_valid_inputs(valid_environment):
>       assert valid_environment.config_dir == Path('/tmp/config')
E       assert '/tmp/config' == PosixPath('/tmp/config')
E        +  where '/tmp/config' = <Environment {'apply_warnings_filter': <function Environment.apply_warnings_filter at 0x7f340e12e2a0>,\n 'args': Namesp...IO name=6 mode='rb+' closefd=True>" mode='r+' encoding='utf-8'>,\n 'stdout_encoding': 'utf-8',\n 'stdout_isatty': False}>.config_dir
E        +  and   PosixPath('/tmp/config') = Path('/tmp/config')

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_context_Environment___init___0_test_valid_inputs.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_context_Environment___init___0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.09s ===============================
"""