
import pytest
from isort._vendored.tomli._parser import parse_inline_table, suffixed_err

def test_invalid_input():
    src = "{key1= 'value1', key2= 3.14"  # Unclosed inline table
    pos = 0
    parse_float = float
    
    with pytest.raises(suffixed_err) as excinfo:
        parse_inline_table(src, pos, parse_float)
    assert str(excinfo.value) == "Unclosed inline table"

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_inline_table_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        src = "{key1= 'value1', key2= 3.14"  # Unclosed inline table
        pos = 0
        parse_float = float
    
>       with pytest.raises(suffixed_err) as excinfo:
E       TypeError: 'function' object is not iterable

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_inline_table_2_test_invalid_input.py:10: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_inline_table_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.12s ===============================
"""