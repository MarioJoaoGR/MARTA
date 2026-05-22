
import pytest
from httpie.cli.nested_json.parse import check_escaped_int, BACKSLASH

def test_none_input():
    with pytest.raises(ValueError) as e:
        check_escaped_int(None)
    assert str(e.value) == 'Not an escaped int'

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

httpie/Test4DT_tests_codestral/test_httpie_cli_nested_json_parse_check_escaped_int_6_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        with pytest.raises(ValueError) as e:
>           check_escaped_int(None)

httpie/Test4DT_tests_codestral/test_httpie_cli_nested_json_parse_check_escaped_int_6_test_none_input.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

value = None

    def check_escaped_int(value: str) -> str:
>       if not value.startswith(BACKSLASH):
E       AttributeError: 'NoneType' object has no attribute 'startswith'

httpie/httpie/cli/nested_json/parse.py:182: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_cli_nested_json_parse_check_escaped_int_6_test_none_input.py::test_none_input
============================== 1 failed in 0.15s ===============================
"""