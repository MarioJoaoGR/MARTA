
import pytest
from unittest.mock import patch
import argparse
from httpie.cli.argtypes import readable_file_arg

@pytest.mark.parametrize("filename", ["nonexistent.txt"])
def test_invalid_file(filename):
    with patch('builtins.open', side_effect=FileNotFoundError("No such file or directory")):
        with pytest.raises(argparse.ArgumentTypeError) as excinfo:
            readable_file_arg(filename)
    assert str(excinfo.value) == f'{filename}: No such file or directory'

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argtypes_readable_file_arg_5_test_invalid_file.py F [100%]

=================================== FAILURES ===================================
______________________ test_invalid_file[nonexistent.txt] ______________________

filename = 'nonexistent.txt'

    @pytest.mark.parametrize("filename", ["nonexistent.txt"])
    def test_invalid_file(filename):
        with patch('builtins.open', side_effect=FileNotFoundError("No such file or directory")):
            with pytest.raises(argparse.ArgumentTypeError) as excinfo:
                readable_file_arg(filename)
>       assert str(excinfo.value) == f'{filename}: No such file or directory'
E       AssertionError: assert 'None: None' == 'nonexistent.... or directory'
E         
E         - nonexistent.txt: No such file or directory
E         + None: None

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argtypes_readable_file_arg_5_test_invalid_file.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argtypes_readable_file_arg_5_test_invalid_file.py::test_invalid_file[nonexistent.txt]
============================== 1 failed in 0.25s ===============================
"""