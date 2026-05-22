
import pytest
from httpie.context import Environment
import sys
from unittest.mock import patch

@pytest.fixture(scope="function")
def environment():
    return Environment()

def test_devnull_is_callable(environment):
    with patch('httpie.context.os') as mock_os:
        mock_os.devnull = 'mocked_devnull'
        assert callable(environment.devnull)

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

httpie/Test4DT_tests_codestral/test_httpie_context_Environment_devnull_1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
___________________________ test_devnull_is_callable ___________________________

environment = <Environment {'apply_warnings_filter': <function Environment.apply_warnings_filter at 0x7f8f59372ca0>,
 'args': Namesp...IO name=6 mode='rb+' closefd=True>" mode='r+' encoding='utf-8'>,
 'stdout_encoding': 'utf-8',
 'stdout_isatty': False}>

    def test_devnull_is_callable(environment):
        with patch('httpie.context.os') as mock_os:
            mock_os.devnull = 'mocked_devnull'
>           assert callable(environment.devnull)
E           assert False
E            +  where False = callable(<_io.TextIOWrapper name='mocked_devnull' mode='w+' encoding='utf-8'>)
E            +    where <_io.TextIOWrapper name='mocked_devnull' mode='w+' encoding='utf-8'> = <Environment {'apply_warnings_filter': <function Environment.apply_warnings_filter at 0x7f8f59372ca0>,\n 'args': Namesp...IO name=6 mode='rb+' closefd=True>" mode='r+' encoding='utf-8'>,\n 'stdout_encoding': 'utf-8',\n 'stdout_isatty': False}>.devnull

httpie/Test4DT_tests_codestral/test_httpie_context_Environment_devnull_1_test_edge_cases.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_context_Environment_devnull_1_test_edge_cases.py::test_devnull_is_callable
============================== 1 failed in 0.23s ===============================
"""