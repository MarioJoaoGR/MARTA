
import pytest
from isort._vendored.tomli._parser import parse_basic_str_escape, TOMLDecodeError, Pos

def test_valid_input():
    src = 'This is a test string without any escape sequences'
    pos = Pos(0)
    with pytest.raises(TOMLDecodeError) as excinfo:
        parse_basic_str_escape(src, pos)
    assert str(excinfo.value) == "Unescaped \\ in a string (at line 1, column 3)"

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_multiline_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        src = 'This is a test string without any escape sequences'
        pos = Pos(0)
        with pytest.raises(TOMLDecodeError) as excinfo:
            parse_basic_str_escape(src, pos)
>       assert str(excinfo.value) == "Unescaped \\ in a string (at line 1, column 3)"
E       assert 'Unescaped "\... 1, column 3)' == 'Unescaped \\... 1, column 3)'
E         
E         - Unescaped \ in a string (at line 1, column 3)
E         + Unescaped "\" in a string (at line 1, column 3)
E         ?           + +

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_multiline_0_test_valid_input.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_multiline_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.10s ===============================
"""