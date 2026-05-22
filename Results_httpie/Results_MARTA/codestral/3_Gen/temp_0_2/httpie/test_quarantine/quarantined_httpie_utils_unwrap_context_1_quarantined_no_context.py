
import pytest
from unittest.mock import patch
from httpie.utils import unwrap_context

def test_no_context():
    try:
        raise ValueError("Root error") from FileNotFoundError("Related error")
    except ValueError as e:
        with patch('httpie.utils.unwrap_context', return_value=e):
            unwrapped_exc = unwrap_context(e)
            assert isinstance(unwrapped_exc, ValueError), "Expected a ValueError"
            assert not hasattr(unwrapped_exc, '__context__'), "Expected no nested exceptions"

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

httpie/Test4DT_tests_codestral/test_httpie_utils_unwrap_context_1_test_no_context.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_no_context ________________________________
FileNotFoundError: Related error

The above exception was the direct cause of the following exception:

    def test_no_context():
        try:
>           raise ValueError("Root error") from FileNotFoundError("Related error")
E           ValueError: Root error

httpie/Test4DT_tests_codestral/test_httpie_utils_unwrap_context_1_test_no_context.py:8: ValueError

During handling of the above exception, another exception occurred:

    def test_no_context():
        try:
            raise ValueError("Root error") from FileNotFoundError("Related error")
        except ValueError as e:
            with patch('httpie.utils.unwrap_context', return_value=e):
                unwrapped_exc = unwrap_context(e)
                assert isinstance(unwrapped_exc, ValueError), "Expected a ValueError"
>               assert not hasattr(unwrapped_exc, '__context__'), "Expected no nested exceptions"
E               AssertionError: Expected no nested exceptions
E               assert not True
E                +  where True = hasattr(ValueError('Root error'), '__context__')

httpie/Test4DT_tests_codestral/test_httpie_utils_unwrap_context_1_test_no_context.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_utils_unwrap_context_1_test_no_context.py::test_no_context
============================== 1 failed in 0.13s ===============================
"""