
import pytest
from isort._vendored.tomli._parser import parse_basic_str, suffixed_err
from isort._vendored.tomli._parser import Pos

def test_invalid_unterminated():
    src = '"Hello, World'
    with pytest.raises(suffixed_err) as exc_info:
        parse_basic_str(src, Pos(0), multiline=False)
    assert "Unterminated string" in str(exc_info.value)

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_0_test_invalid_unterminated.py F [100%]

=================================== FAILURES ===================================
__________________________ test_invalid_unterminated ___________________________

    def test_invalid_unterminated():
        src = '"Hello, World'
>       with pytest.raises(suffixed_err) as exc_info:
E       TypeError: 'function' object is not iterable

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_0_test_invalid_unterminated.py:8: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_0_test_invalid_unterminated.py::test_invalid_unterminated
============================== 1 failed in 0.13s ===============================
"""