
import pytest
from httpie.cli.dicts import HTTPHeadersDict
from unittest.mock import patch

def test_valid_input():
    headers = HTTPHeadersDict()
    headers.add('Content-Type', 'application/json')
    headers.add('Set-Cookie', 'cookie1=value1;')
    headers.add('Cache-Control', None)
    
    with patch.object(HTTPHeadersDict, 'popall', return_value=['application/json']):
        headers.remove_item('Content-Type', 'application/json')
        assert 'Content-Type' not in headers

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_dicts_HTTPHeadersDict_remove_item_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        headers = HTTPHeadersDict()
        headers.add('Content-Type', 'application/json')
        headers.add('Set-Cookie', 'cookie1=value1;')
        headers.add('Cache-Control', None)
    
        with patch.object(HTTPHeadersDict, 'popall', return_value=['application/json']):
            headers.remove_item('Content-Type', 'application/json')
>           assert 'Content-Type' not in headers
E           AssertionError: assert 'Content-Type' not in <HTTPHeadersDict('Content-Type': 'application/json', 'Set-Cookie': 'cookie1=value1;', 'Cache-Control': None)>

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_dicts_HTTPHeadersDict_remove_item_0_test_valid_input.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_dicts_HTTPHeadersDict_remove_item_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.10s ===============================
"""