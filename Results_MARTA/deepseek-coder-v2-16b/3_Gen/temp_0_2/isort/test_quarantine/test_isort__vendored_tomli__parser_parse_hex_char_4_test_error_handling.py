
import pytest
from isort._vendored.tomli._parser import parse_hex_char, HEXDIGIT_CHARS, is_unicode_scalar_value
from typing import Tuple

def test_parse_hex_char():
    # Test case with valid hex value
    src = "1a3f"
    pos = 0
    hex_len = 2
    new_pos, char = parse_hex_char(src, pos, hex_len)
    assert new_pos == 2
    assert char == '\x1a'
    
    # Test case with invalid hex value length
    src = "1a3f"
    pos = 0
    hex_len = 3
    with pytest.raises(ValueError):
        parse_hex_char(src, pos, hex_len)

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_hex_char_4_test_error_handling.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_parse_hex_char ______________________________

    def test_parse_hex_char():
        # Test case with valid hex value
        src = "1a3f"
        pos = 0
        hex_len = 2
        new_pos, char = parse_hex_char(src, pos, hex_len)
        assert new_pos == 2
        assert char == '\x1a'
    
        # Test case with invalid hex value length
        src = "1a3f"
        pos = 0
        hex_len = 3
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_hex_char_4_test_error_handling.py:19: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_hex_char_4_test_error_handling.py::test_parse_hex_char
============================== 1 failed in 0.13s ===============================
"""