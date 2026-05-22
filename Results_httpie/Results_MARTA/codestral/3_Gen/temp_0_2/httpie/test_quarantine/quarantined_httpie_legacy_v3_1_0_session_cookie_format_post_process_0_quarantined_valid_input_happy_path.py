
import pytest
from httpie.legacy.v3_1_0_session_cookie_format import post_process
from typing import List, Dict, Any, Type

def test_valid_input_happy_path():
    # Test when original_type is dict
    result = post_process(
        [{'name': 'cookie1', 'value': 'value1'}, {'name': 'cookie2', 'value': 'value2'}],
        original_type=dict
    )
    assert result == {
        'cookie1': {'name': 'cookie1', 'value': 'value1'},
        'cookie2': {'name': 'cookie2', 'value': 'value2'}
    }

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

httpie/Test4DT_tests_codestral/test_httpie_legacy_v3_1_0_session_cookie_format_post_process_0_test_valid_input_happy_path.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_happy_path __________________________

    def test_valid_input_happy_path():
        # Test when original_type is dict
        result = post_process(
            [{'name': 'cookie1', 'value': 'value1'}, {'name': 'cookie2', 'value': 'value2'}],
            original_type=dict
        )
>       assert result == {
            'cookie1': {'name': 'cookie1', 'value': 'value1'},
            'cookie2': {'name': 'cookie2', 'value': 'value2'}
        }
E       AssertionError: assert {'cookie1': {...e': 'value2'}} == {'cookie1': {...e': 'value2'}}
E         
E         Differing items:
E         {'cookie1': {'value': 'value1'}} != {'cookie1': {'name': 'cookie1', 'value': 'value1'}}
E         {'cookie2': {'value': 'value2'}} != {'cookie2': {'name': 'cookie2', 'value': 'value2'}}
E         Use -v to get more diff

httpie/Test4DT_tests_codestral/test_httpie_legacy_v3_1_0_session_cookie_format_post_process_0_test_valid_input_happy_path.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_legacy_v3_1_0_session_cookie_format_post_process_0_test_valid_input_happy_path.py::test_valid_input_happy_path
============================== 1 failed in 0.10s ===============================
"""