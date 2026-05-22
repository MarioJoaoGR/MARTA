
import pytest
from httpie.cli.argtypes import readable_file_arg
import argparse

def test_none_input():
    with pytest.raises(argparse.ArgumentTypeError) as excinfo:
        readable_file_arg(None)
    assert str(excinfo.value) == "None: expected str, bytes or os.PathLike object"

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argtypes_readable_file_arg_1_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        with pytest.raises(argparse.ArgumentTypeError) as excinfo:
>           readable_file_arg(None)

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argtypes_readable_file_arg_1_test_none_input.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

filename = None

    def readable_file_arg(filename):
        try:
>           with open(filename, 'rb'):
E           TypeError: expected str, bytes or os.PathLike object, not NoneType

httpie/httpie/cli/argtypes.py:196: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argtypes_readable_file_arg_1_test_none_input.py::test_none_input
============================== 1 failed in 0.19s ===============================
"""