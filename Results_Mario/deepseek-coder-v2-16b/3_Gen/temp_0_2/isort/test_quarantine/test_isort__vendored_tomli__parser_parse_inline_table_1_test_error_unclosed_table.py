
import pytest
from isort._vendored.tomli._parser import parse_inline_table, suffixed_err
from typing import Tuple, Callable

# Assuming Pos and ParseFloat are defined elsewhere in the module or imported from a library
Pos = int  # Example definition for Pos
ParseFloat = Callable[[str], float]

def test_error_unclosed_table():
    src = "{key1= 'value1', key2= 3.14, }"
    with pytest.raises(suffixed_err) as excinfo:
        parse_inline_table(src, 0, float)
    
    assert "Unclosed inline table" in str(excinfo.value)

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_inline_table_1_test_error_unclosed_table.py F [100%]

=================================== FAILURES ===================================
__________________________ test_error_unclosed_table ___________________________

    def test_error_unclosed_table():
        src = "{key1= 'value1', key2= 3.14, }"
>       with pytest.raises(suffixed_err) as excinfo:
E       TypeError: 'function' object is not iterable

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_inline_table_1_test_error_unclosed_table.py:12: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_inline_table_1_test_error_unclosed_table.py::test_error_unclosed_table
============================== 1 failed in 0.10s ===============================
"""