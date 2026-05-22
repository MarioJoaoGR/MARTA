
import pytest
from unittest.mock import patch
from httpie.cli.nested_json.errors import NestedJSONSyntaxError

def test_valid_input():
    source = '{"key": [1, 2, {"innerKey": "value"}]}'
    
    with pytest.raises(NestedJSONSyntaxError) as exc_info:
        raise NestedJSONSyntaxError(source=source, token=None, message="Invalid nested structure detected.")
    
    assert str(exc_info.value) == 'Invalid nested structure detected.'

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_nested_json_errors_NestedJSONSyntaxError___init___0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        source = '{"key": [1, 2, {"innerKey": "value"}]}'
    
        with pytest.raises(NestedJSONSyntaxError) as exc_info:
            raise NestedJSONSyntaxError(source=source, token=None, message="Invalid nested structure detected.")
    
>       assert str(exc_info.value) == 'Invalid nested structure detected.'
E       AssertionError: assert 'HTTPie Synta...ure detected.' == 'Invalid nest...ure detected.'
E         
E         - Invalid nested structure detected.
E         + HTTPie Syntax Error: Invalid nested structure detected.
E         ? +++++++++++++++++++++

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_nested_json_errors_NestedJSONSyntaxError___init___0_test_valid_input.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_nested_json_errors_NestedJSONSyntaxError___init___0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.06s ===============================
"""