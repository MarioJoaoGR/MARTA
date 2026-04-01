
import pytest
from isort._vendored.tomli._parser import parse_inline_table, suffixed_err

def test_valid_input():
    src = 'key1=value1 key2={} key3=3.14'
    pos = 0
    with pytest.raises(suffixed_err):
        parse_inline_table(src, pos, float)

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_inline_table_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        src = 'key1=value1 key2={} key3=3.14'
        pos = 0
>       with pytest.raises(suffixed_err):
E       TypeError: 'function' object is not iterable

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_inline_table_0_test_valid_input.py:8: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_inline_table_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.10s ===============================
"""