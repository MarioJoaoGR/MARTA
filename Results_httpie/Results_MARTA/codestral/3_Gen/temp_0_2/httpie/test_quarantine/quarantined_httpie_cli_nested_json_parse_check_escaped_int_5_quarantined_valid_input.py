
import pytest
from unittest.mock import patch
from httpie.cli.nested_json.parse import check_escaped_int

def test_valid_input():
    with patch('builtins.print'):  # Mocking print to avoid actual output in tests
        assert check_escaped_int('\123') == '123'

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

httpie/Test4DT_tests_codestral/test_httpie_cli_nested_json_parse_check_escaped_int_5_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        with patch('builtins.print'):  # Mocking print to avoid actual output in tests
>           assert check_escaped_int('\123') == '123'

httpie/Test4DT_tests_codestral/test_httpie_cli_nested_json_parse_check_escaped_int_5_test_valid_input.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

value = 'S'

    def check_escaped_int(value: str) -> str:
        if not value.startswith(BACKSLASH):
>           raise ValueError('Not an escaped int')
E           ValueError: Not an escaped int

httpie/httpie/cli/nested_json/parse.py:183: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_cli_nested_json_parse_check_escaped_int_5_test_valid_input.py::test_valid_input
============================== 1 failed in 0.14s ===============================
"""