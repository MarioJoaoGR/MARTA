
import pytest
from isort._vendored.tomli._parser import parse_basic_str_escape, suffixed_err

def test_edge_case_multiline():
    src = 'hello\\nworld'
    pos = 0
    with pytest.raises(suffixed_err) as excinfo:
        parse_basic_str_escape(src, pos, multiline=True)
    assert str(excinfo.value) == "Unescaped \"\\\\\" in a string"

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0_test_edge_case_multiline.py F [100%]

=================================== FAILURES ===================================
___________________________ test_edge_case_multiline ___________________________

    def test_edge_case_multiline():
        src = 'hello\\nworld'
        pos = 0
>       with pytest.raises(suffixed_err) as excinfo:
E       TypeError: 'function' object is not iterable

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0_test_edge_case_multiline.py:8: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0_test_edge_case_multiline.py::test_edge_case_multiline
============================== 1 failed in 0.11s ===============================
"""