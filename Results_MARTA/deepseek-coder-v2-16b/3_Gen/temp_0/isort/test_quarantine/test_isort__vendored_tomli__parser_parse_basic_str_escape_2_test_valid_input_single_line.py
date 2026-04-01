
import pytest
from isort._vendored.tomli._parser import parse_basic_str_escape, Pos, suffixed_err

def test_valid_input_single_line():
    src = 'Hello\nWorld'
    pos = Pos(0)
    with pytest.raises(suffixed_err):
        parse_basic_str_escape(src, pos)

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_2_test_valid_input_single_line.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_single_line _________________________

    def test_valid_input_single_line():
        src = 'Hello\nWorld'
        pos = Pos(0)
>       with pytest.raises(suffixed_err):
E       TypeError: 'function' object is not iterable

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_2_test_valid_input_single_line.py:8: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_2_test_valid_input_single_line.py::test_valid_input_single_line
============================== 1 failed in 0.13s ===============================
"""