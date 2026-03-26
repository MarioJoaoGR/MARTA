
from isort._vendored.tomli._parser import parse_key, Pos, Key, TOML_WS
from typing import Tuple, Optional

def skip_chars(src: str, pos: int, chars: str) -> int:
    while pos < len(src) and src[pos] in chars:
        pos += 1
    return pos

# Assuming the implementation of parse_key_part is correct and available here.
def parse_key_part(src: str, pos: Pos) -> Tuple[Pos, Key]:
    start = pos
    while pos < len(src) and src[pos] not in ('.', ' ', '\n', '\r'):
        pos += 1
    return pos, src[start:pos]

def test_empty_string():
    src = ""
    pos = 0
    new_pos, key = parse_key(src, pos)
    assert new_pos == 0
    assert key == ()

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_1_test_empty_string.py F [100%]

=================================== FAILURES ===================================
______________________________ test_empty_string _______________________________

    def test_empty_string():
        src = ""
        pos = 0
>       new_pos, key = parse_key(src, pos)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_1_test_empty_string.py:20: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/_vendored/tomli/_parser.py:358: in parse_key
    pos, key_part = parse_key_part(src, pos)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = '', pos = 0

    def parse_key_part(src: str, pos: Pos) -> Tuple[Pos, str]:
        try:
            char: Optional[str] = src[pos]
        except IndexError:
            char = None
        if char in BARE_KEY_CHARS:
            start_pos = pos
            pos = skip_chars(src, pos, BARE_KEY_CHARS)
            return pos, src[start_pos:pos]
        if char == "'":
            return parse_literal_str(src, pos)
        if char == '"':
            return parse_one_line_basic_str(src, pos)
>       raise suffixed_err(src, pos, "Invalid initial character for a key part")
E       isort._vendored.tomli._parser.TOMLDecodeError: Invalid initial character for a key part (at end of document)

isort/isort/_vendored/tomli/_parser.py:388: TOMLDecodeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_1_test_empty_string.py::test_empty_string
============================== 1 failed in 0.12s ===============================
"""