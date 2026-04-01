
import pytest
from isort._vendored.tomli._parser import parse_key_value_pair, suffixed_err

def test_edge_case_none_input():
    src = None
    pos = 0
    parse_float = float

    with pytest.raises(TypeError) as excinfo:
        new_pos, key, value = parse_key_value_pair(src, pos, parse_float)

    assert str(excinfo.value) == "Expected string or bytes-like object, not NoneType"

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_value_pair_2_test_edge_case_none_input.py F [100%]

=================================== FAILURES ===================================
__________________________ test_edge_case_none_input ___________________________

    def test_edge_case_none_input():
        src = None
        pos = 0
        parse_float = float
    
        with pytest.raises(TypeError) as excinfo:
            new_pos, key, value = parse_key_value_pair(src, pos, parse_float)
    
>       assert str(excinfo.value) == "Expected string or bytes-like object, not NoneType"
E       assert "'NoneType' o...subscriptable" == 'Expected str... not NoneType'
E         
E         - Expected string or bytes-like object, not NoneType
E         + 'NoneType' object is not subscriptable

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_value_pair_2_test_edge_case_none_input.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_value_pair_2_test_edge_case_none_input.py::test_edge_case_none_input
============================== 1 failed in 0.12s ===============================
"""