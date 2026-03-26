
import pytest
from typing import Tuple
from isort._vendored.tomli._parser import Pos

def parse_multiline_str(src: str, pos: Pos, *, literal: bool) -> Tuple[Pos, str]:
    if literal:
        delim = "'" if src.startswith("'''") else '"'
        end_pos = skip_until(
            src,
            pos,
            delim * 3,
            error_on=ILLEGAL_MULTILINE_LITERAL_STR_CHARS,
            error_on_eof=True,
        )
        result = src[pos:end_pos]
        pos = end_pos + len(delim)
    else:
        delim = '"'
        pos, result = parse_basic_str(src, pos, multiline=True)

    # Add at maximum two extra apostrophes/quotes if the end sequence
    # is 4 or 5 chars long instead of just 3.
    if not src.startswith(delim, pos):
        return pos, result
    pos += 1
    if not src.startswith(delim, pos):
        return pos, result + delim
    pos += 1
    return pos, result + (delim * 2)

def skip_until(src: str, pos: int, seq: str, *, error_on=None, error_on_eof: bool = False) -> int:
    while True:
        next_pos = src.find(seq, pos)
        if next_pos == -1:
            if error_on_eof:
                raise ValueError("Unterminated string literal")
            return len(src)
        if all(ord(src[i]) < 32 or ord(src[i]) > 126 for i in range(pos, next_pos)):
            pos = next_pos + len(seq)
            continue
        return next_pos

ILLEGAL_MULTILINE_LITERAL_STR_CHARS = set()

def test_valid_basic_multiline_string():
    src = '"""this is a test"""'
    pos, parsed_str = parse_multiline_str(src, Pos(0), literal=False)
    assert parsed_str == "this is a test"
    assert pos == len(src)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_multiline_str_0_test_valid_basic_multiline_string
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_0_test_valid_basic_multiline_string.py:20:22: E0602: Undefined variable 'parse_basic_str' (undefined-variable)


"""