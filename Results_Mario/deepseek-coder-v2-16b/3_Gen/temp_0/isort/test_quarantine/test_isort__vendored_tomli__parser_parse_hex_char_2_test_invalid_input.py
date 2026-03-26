
from isort._vendored.tomli._parser import parse_hex_char
import pytest

def test_invalid_input():
    with pytest.raises(ValueError) as excinfo:
        src = "Hello, world!"
        pos = 7
        hex_len = 2
        parse_hex_char(src, pos, hex_len)
    
    assert str(excinfo.value) == 'Invalid hex value'

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_hex_char_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(ValueError) as excinfo:
            src = "Hello, world!"
            pos = 7
            hex_len = 2
            parse_hex_char(src, pos, hex_len)
    
>       assert str(excinfo.value) == 'Invalid hex value'
E       AssertionError: assert 'Invalid hex ... 1, column 8)' == 'Invalid hex value'
E         
E         - Invalid hex value
E         + Invalid hex value (at line 1, column 8)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_hex_char_2_test_invalid_input.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_hex_char_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.14s ===============================
"""