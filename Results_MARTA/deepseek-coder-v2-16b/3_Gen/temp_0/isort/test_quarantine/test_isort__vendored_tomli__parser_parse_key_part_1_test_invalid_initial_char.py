
from isort._vendored.tomli._parser import parse_key_part, BARE_KEY_CHARS, Pos, suffixed_err
from typing import Tuple, Optional

def skip_chars(src: str, pos: Pos, chars: str) -> Pos:
    while pos < len(src) and src[pos] in chars:
        pos += 1
    return pos

def parse_literal_str(src: str, pos: Pos) -> Tuple[Pos, str]:
    if pos >= len(src) or src[pos] != "'":
        raise ValueError("Expected single quote at the start of a literal string")
    start = pos + 1
    while pos < len(src) and src[pos] != "'":
        pos += 1
    return pos, src[start:pos]

def parse_one_line_basic_str(src: str, pos: Pos) -> Tuple[Pos, str]:
    if pos >= len(src) or src[pos] != '"':
        raise ValueError("Expected double quote at the start of a basic string")
    start = pos + 1
    while pos < len(src) and src[pos] != '"':
        pos += 1
    return pos, src[start:pos]

def test_invalid_initial_char():
    # Test case for invalid initial character for a key part
    src = "!key"
    pos = Pos(0)
    try:
        new_pos, parsed_key = parse_key_part(src, pos)
        assert False, "Expected ValueError but got no exception"
    except ValueError as e:
        assert str(e) == "Invalid initial character for a key part", f"Unexpected error message: {str(e)}"

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_1_test_invalid_initial_char.py F [100%]

=================================== FAILURES ===================================
__________________________ test_invalid_initial_char ___________________________

    def test_invalid_initial_char():
        # Test case for invalid initial character for a key part
        src = "!key"
        pos = Pos(0)
        try:
>           new_pos, parsed_key = parse_key_part(src, pos)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_1_test_invalid_initial_char.py:31: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = '!key', pos = 0

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
E       isort._vendored.tomli._parser.TOMLDecodeError: Invalid initial character for a key part (at line 1, column 1)

isort/isort/_vendored/tomli/_parser.py:388: TOMLDecodeError

During handling of the above exception, another exception occurred:

    def test_invalid_initial_char():
        # Test case for invalid initial character for a key part
        src = "!key"
        pos = Pos(0)
        try:
            new_pos, parsed_key = parse_key_part(src, pos)
            assert False, "Expected ValueError but got no exception"
        except ValueError as e:
>           assert str(e) == "Invalid initial character for a key part", f"Unexpected error message: {str(e)}"
E           AssertionError: Unexpected error message: Invalid initial character for a key part (at line 1, column 1)
E           assert 'Invalid init... 1, column 1)' == 'Invalid init...or a key part'
E             
E             - Invalid initial character for a key part
E             + Invalid initial character for a key part (at line 1, column 1)
E             ?                                         ++++++++++++++++++++++

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_1_test_invalid_initial_char.py:34: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_1_test_invalid_initial_char.py::test_invalid_initial_char
============================== 1 failed in 0.16s ===============================
"""