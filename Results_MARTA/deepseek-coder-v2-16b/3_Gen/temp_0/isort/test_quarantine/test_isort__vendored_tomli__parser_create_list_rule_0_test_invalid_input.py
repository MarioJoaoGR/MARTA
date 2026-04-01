
from isort._vendored.tomli._parser import create_list_rule, Pos, Output
from isort._vendored.tomli._parser import Flags, suffixed_err
import pytest

def test_invalid_input():
    src = "[["  # Unterminated string literal
    pos = Pos(0)
    out = Output()
    
    with pytest.raises(suffixed_err) as excinfo:
        create_list_rule(src, pos, out)
    
    assert "Expected ']]' at the end of an array declaration" in str(excinfo.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort__vendored_tomli__parser_create_list_rule_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        src = "[["  # Unterminated string literal
        pos = Pos(0)
>       out = Output()
E       TypeError: Output.__new__() missing 2 required positional arguments: 'data' and 'flags'

isort/Test4DT_tests/test_isort__vendored_tomli__parser_create_list_rule_0_test_invalid_input.py:9: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_create_list_rule_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.18s ===============================
"""