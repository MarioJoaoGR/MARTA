
import pytest
from httpie.context import Environment

def test_valid_inputs():
    env = Environment()
    assert callable(env.rich_error_console)

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

httpie/Test4DT_tests_codestral/test_httpie_context_Environment_rich_error_console_1_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        env = Environment()
>       assert callable(env.rich_error_console)
E       assert False
E        +  where False = callable(<console width=80 None>)
E        +    where <console width=80 None> = <Environment {'apply_warnings_filter': <function Environment.apply_warnings_filter at 0x7fc79696f4c0>,\n 'args': Namesp...IO name=6 mode='rb+' closefd=True>" mode='r+' encoding='utf-8'>,\n 'stdout_encoding': 'utf-8',\n 'stdout_isatty': False}>.rich_error_console

httpie/Test4DT_tests_codestral/test_httpie_context_Environment_rich_error_console_1_test_valid_inputs.py:7: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_context_Environment_rich_error_console_1_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.22s ===============================
"""