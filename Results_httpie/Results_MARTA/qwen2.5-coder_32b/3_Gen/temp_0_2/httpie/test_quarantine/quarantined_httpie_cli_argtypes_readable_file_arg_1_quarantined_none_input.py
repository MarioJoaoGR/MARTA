
import pytest
import argparse
from httpie.cli.argtypes import readable_file_arg

def test_none_input():
    with pytest.raises(argparse.ArgumentTypeError) as excinfo:
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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argtypes_readable_file_arg_1_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        with pytest.raises(argparse.ArgumentTypeError) as excinfo:
>           readable_file_arg(None)

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argtypes_readable_file_arg_1_test_none_input.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

filename = None

    def readable_file_arg(filename):
        try:
>           with open(filename, 'rb'):
E           TypeError: expected str, bytes or os.PathLike object, not NoneType

httpie/httpie/cli/argtypes.py:196: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argtypes_readable_file_arg_1_test_none_input.py::test_none_input
============================== 1 failed in 0.17s ===============================
"""