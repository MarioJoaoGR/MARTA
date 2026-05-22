
import pytest
from httpie.cli.dicts import HTTPHeadersDict

def test_valid_input():
    headers = HTTPHeadersDict()
    
    # Add a valid key-value pair
    headers.add('Content-Type', 'application/json')
    assert 'Content-Type' in headers
    assert headers['Content-Type'] == ['application/json']

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_dicts_HTTPHeadersDict_remove_item_1_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        headers = HTTPHeadersDict()
    
        # Add a valid key-value pair
        headers.add('Content-Type', 'application/json')
        assert 'Content-Type' in headers
>       assert headers['Content-Type'] == ['application/json']
E       AssertionError: assert 'application/json' == ['application/json']

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_dicts_HTTPHeadersDict_remove_item_1_test_valid_input.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_dicts_HTTPHeadersDict_remove_item_1_test_valid_input.py::test_valid_input
============================== 1 failed in 0.14s ===============================
"""