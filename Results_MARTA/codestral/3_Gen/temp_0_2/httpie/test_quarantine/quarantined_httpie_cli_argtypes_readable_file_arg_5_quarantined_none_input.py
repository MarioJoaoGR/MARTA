
import pytest
from unittest.mock import patch
import argparse
from httpie.cli.argtypes import readable_file_arg

def test_none_input():
    with pytest.raises(argparse.ArgumentTypeError) as excinfo:
        with patch('builtins.open', side_effect=FileNotFoundError("No such file or directory")):
            readable_file_arg(None)
    assert str(excinfo.value) == "None: No such file or directory"

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

httpie/Test4DT_tests_codestral/test_httpie_cli_argtypes_readable_file_arg_5_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        with pytest.raises(argparse.ArgumentTypeError) as excinfo:
            with patch('builtins.open', side_effect=FileNotFoundError("No such file or directory")):
                readable_file_arg(None)
>       assert str(excinfo.value) == "None: No such file or directory"
E       AssertionError: assert 'None: None' == 'None: No suc... or directory'
E         
E         - None: No such file or directory
E         + None: None

httpie/Test4DT_tests_codestral/test_httpie_cli_argtypes_readable_file_arg_5_test_none_input.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_cli_argtypes_readable_file_arg_5_test_none_input.py::test_none_input
============================== 1 failed in 0.24s ===============================
"""