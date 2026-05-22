
import pytest
from httpie.context import Environment
from pathlib import Path
import sys
from unittest.mock import patch

@pytest.fixture(scope="function")
def valid_environment():
    return Environment()

def test_valid_inputs(valid_environment):
    with patch('httpie.context.DEFAULT_CONFIG_DIR', Path('/tmp/config')):
        assert valid_environment.config_dir == Path('/tmp/config')

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

httpie/Test4DT_tests_codestral/test_httpie_context_Environment___init___0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

valid_environment = <Environment {'apply_warnings_filter': <function Environment.apply_warnings_filter at 0x7f281ab7ef20>,
 'args': Namesp...IO name=6 mode='rb+' closefd=True>" mode='r+' encoding='utf-8'>,
 'stdout_encoding': 'utf-8',
 'stdout_isatty': False}>

    def test_valid_inputs(valid_environment):
        with patch('httpie.context.DEFAULT_CONFIG_DIR', Path('/tmp/config')):
>           assert valid_environment.config_dir == Path('/tmp/config')
E           assert PosixPath('/home/joaovitorino/.config/httpie') == PosixPath('/tmp/config')
E            +  where PosixPath('/home/joaovitorino/.config/httpie') = <Environment {'apply_warnings_filter': <function Environment.apply_warnings_filter at 0x7f281ab7ef20>,\n 'args': Namesp...IO name=6 mode='rb+' closefd=True>" mode='r+' encoding='utf-8'>,\n 'stdout_encoding': 'utf-8',\n 'stdout_isatty': False}>.config_dir
E            +  and   PosixPath('/tmp/config') = Path('/tmp/config')

httpie/Test4DT_tests_codestral/test_httpie_context_Environment___init___0_test_valid_inputs.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_context_Environment___init___0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.10s ===============================
"""