
import pytest
from typing import Tuple

def parse_multiline_str(src: str, pos: int, *, literal: bool) -> Tuple[int, str]:
    pos += 3
    if src.startswith("\n", pos):
        pos += 1

    if literal:
        delim = "'"
        end_pos = skip_until(
            src,
            pos,
            "'''",
            error_on=ILLEGAL_MULTILINE_LITERAL_STR_CHARS,
            error_on_eof=True,
        )
        result = src[pos:end_pos]
        pos = end_pos + 3
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

# Assuming the rest of the function definitions and imports are correctly defined elsewhere in your module

def test_valid_multiline_literal():
    src = 'Hello \\"""world\\"""'
    pos = 0
    new_pos, parsed_str = parse_multiline_str(src, pos, literal=True)
    assert parsed_str == 'Hello "world"'
    assert new_pos == len('Hello \\"""world\\"""')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_multiline_str_0_test_valid_multiline_literal
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_0_test_valid_multiline_literal.py:12:18: E0602: Undefined variable 'skip_until' (undefined-variable)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_0_test_valid_multiline_literal.py:16:21: E0602: Undefined variable 'ILLEGAL_MULTILINE_LITERAL_STR_CHARS' (undefined-variable)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_0_test_valid_multiline_literal.py:23:22: E0602: Undefined variable 'parse_basic_str' (undefined-variable)


"""