
import pytest
from httpie.cli.requestitems import interpret_nested_json

def process_data_nested_json_embed_args(pairs) -> dict:
    return interpret_nested_json(pairs)

def test_valid_input():
    pairs = [("a.b", "SET 2"), ("a", "SET {'c': 3}"), ("a.d", "SET None")]
    expected_output = {'a': {'b': 2, 'c': 3, 'd': None}}
    
    result = process_data_nested_json_embed_args(pairs)
    assert result == expected_output

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

httpie/Test4DT_tests_codestral/test_httpie_cli_requestitems_process_data_nested_json_embed_args_1_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        pairs = [("a.b", "SET 2"), ("a", "SET {'c': 3}"), ("a.d", "SET None")]
        expected_output = {'a': {'b': 2, 'c': 3, 'd': None}}
    
        result = process_data_nested_json_embed_args(pairs)
>       assert result == expected_output
E       assert {'a': "SET {'...': 'SET None'} == {'a': {'b': 2...3, 'd': None}}
E         
E         Differing items:
E         {'a': "SET {'c': 3}"} != {'a': {'b': 2, 'c': 3, 'd': None}}
E         Left contains 2 more items:
E         {'a.b': 'SET 2', 'a.d': 'SET None'}
E         Use -v to get more diff

httpie/Test4DT_tests_codestral/test_httpie_cli_requestitems_process_data_nested_json_embed_args_1_test_valid_input.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_cli_requestitems_process_data_nested_json_embed_args_1_test_valid_input.py::test_valid_input
============================== 1 failed in 0.24s ===============================
"""