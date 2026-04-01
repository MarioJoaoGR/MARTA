
from isort._vendored.tomli._parser import key_value_rule, Output, Pos, Key, ParseFloat
import pytest

def test_valid_input():
    src = 'key=value'
    pos = 0
    out = Output()
    header = ('namespace',)
    parse_float = float
    
    new_pos = key_value_rule(src, pos, out, header, parse_float)
    assert new_pos == len(src)
    assert isinstance(out.data, dict)
    assert out.data['namespace'] == {'key': 'value'}

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_key_value_rule_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        src = 'key=value'
        pos = 0
>       out = Output()
E       TypeError: Output.__new__() missing 2 required positional arguments: 'data' and 'flags'

isort/Test4DT_tests/test_isort__vendored_tomli__parser_key_value_rule_0_test_valid_input.py:8: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_key_value_rule_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.10s ===============================
"""