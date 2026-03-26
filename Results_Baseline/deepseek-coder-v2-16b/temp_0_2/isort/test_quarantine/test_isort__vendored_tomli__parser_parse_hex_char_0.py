
import pytest
from typing import Tuple
from isort._vendored.tomli._parser import parse_hex_char

# Define the HEXDIGIT_CHARS and is_unicode_scalar_value functions for completeness
HEXDIGIT_CHARS = set("0123456789abcdefABCDEF")

def is_unicode_scalar_value(code: int) -> bool:
    return 0 <= code <= 0x10FFFF and (code < 0xD800 or code > 0xDFFF) and (code < 0xFFFE or code > 0xFFFF)

def suffixed_err(src: str, pos: int, msg: str):
    raise ValueError(f"{msg} at position {pos} in source string '{src}'")

# Test cases for parse_hex_char function

@pytest.mark.parametrize("src, pos, hex_len, expected", [
    ("abc123", 0, 6, (6, 'a')),
])
def test_parse_hex_char_basic(src, pos, hex_len, expected):
    result = parse_hex_char(src, pos, hex_len)
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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_hex_char_0.py F [100%]

=================================== FAILURES ===================================
_______________ test_parse_hex_char_basic[abc123-0-6-expected0] ________________

src = 'abc123', pos = 0, hex_len = 6, expected = (6, 'a')

    @pytest.mark.parametrize("src, pos, hex_len, expected", [
        ("abc123", 0, 6, (6, 'a')),
    ])
    def test_parse_hex_char_basic(src, pos, hex_len, expected):
>       result = parse_hex_char(src, pos, hex_len)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_hex_char_0.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = 'abc123', pos = 6, hex_len = 6

    def parse_hex_char(src: str, pos: Pos, hex_len: int) -> Tuple[Pos, str]:
        hex_str = src[pos : pos + hex_len]
        if len(hex_str) != hex_len or not HEXDIGIT_CHARS.issuperset(hex_str):
            raise suffixed_err(src, pos, "Invalid hex value")
        pos += hex_len
        hex_int = int(hex_str, 16)
        if not is_unicode_scalar_value(hex_int):
>           raise suffixed_err(src, pos, "Escaped character is not a Unicode scalar value")
E           isort._vendored.tomli._parser.TOMLDecodeError: Escaped character is not a Unicode scalar value (at end of document)

isort/isort/_vendored/tomli/_parser.py:494: TOMLDecodeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_hex_char_0.py::test_parse_hex_char_basic[abc123-0-6-expected0]
============================== 1 failed in 0.11s ===============================
"""