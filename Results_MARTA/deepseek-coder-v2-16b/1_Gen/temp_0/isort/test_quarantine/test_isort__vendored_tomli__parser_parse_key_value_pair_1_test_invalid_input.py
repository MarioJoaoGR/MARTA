
import pytest
from isort._vendored.tomli._parser import parse_key_value_pair, TOML_WS
from typing import Tuple, Any, Optional

def test_invalid_input():
    src = 'key value'
    pos = 0
    parse_float = float
    
    with pytest.raises(ValueError) as excinfo:
        parse_key_value_pair(src, pos, parse_float)
    
    assert str(excinfo.value) == "Expected '=' after a key in a key/value pair"

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_value_pair_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        src = 'key value'
        pos = 0
        parse_float = float
    
        with pytest.raises(ValueError) as excinfo:
            parse_key_value_pair(src, pos, parse_float)
    
>       assert str(excinfo.value) == "Expected '=' after a key in a key/value pair"
E       assert 'Expected "="... 1, column 5)' == "Expected '='...ey/value pair"
E         
E         - Expected '=' after a key in a key/value pair
E         ?          ^ ^
E         + Expected "=" after a key in a key/value pair (at line 1, column 5)
E         ?          ^ ^                                ++++++++++++++++++++++

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_value_pair_1_test_invalid_input.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_value_pair_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.11s ===============================
"""