
import pytest
from isort._vendored.tomli._parser import parse_multiline_str, Pos

def test_invalid_escape_sequence():
    with pytest.raises(ValueError) as excinfo:
        parse_multiline_str("Hello\\x world", 0, literal=False)
    assert str(excinfo.value) == "Illegal escape sequence \"\\x\" in string"

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_2_test_invalid_escape_sequence.py F [100%]

=================================== FAILURES ===================================
_________________________ test_invalid_escape_sequence _________________________

    def test_invalid_escape_sequence():
        with pytest.raises(ValueError) as excinfo:
            parse_multiline_str("Hello\\x world", 0, literal=False)
>       assert str(excinfo.value) == "Illegal escape sequence \"\\x\" in string"
E       assert 'Unescaped "\... 1, column 8)' == 'Illegal esca...\x" in string'
E         
E         - Illegal escape sequence "\x" in string
E         + Unescaped "\" in a string (at line 1, column 8)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_2_test_invalid_escape_sequence.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_2_test_invalid_escape_sequence.py::test_invalid_escape_sequence
============================== 1 failed in 0.13s ===============================
"""