
import pytest
from httpie.cli.argtypes import SessionNameValidator
import argparse

def test_invalid_session_name():
    validator = SessionNameValidator("Invalid session name.")
    with pytest.raises(argparse.ArgumentError):
        validator("invalid-session/name")  # This should raise an ArgumentError

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argtypes_SessionNameValidator___call___0_test_invalid_session_name.py F [100%]

=================================== FAILURES ===================================
__________________________ test_invalid_session_name ___________________________

    def test_invalid_session_name():
        validator = SessionNameValidator("Invalid session name.")
>       with pytest.raises(argparse.ArgumentError):
E       Failed: DID NOT RAISE <class 'argparse.ArgumentError'>

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argtypes_SessionNameValidator___call___0_test_invalid_session_name.py:8: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argtypes_SessionNameValidator___call___0_test_invalid_session_name.py::test_invalid_session_name
============================== 1 failed in 0.22s ===============================
"""