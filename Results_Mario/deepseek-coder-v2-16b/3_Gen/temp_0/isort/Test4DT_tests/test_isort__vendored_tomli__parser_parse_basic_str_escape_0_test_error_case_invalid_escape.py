
import pytest
from isort._vendored.tomli._parser import parse_basic_str_escape, Pos, BASIC_STR_ESCAPE_REPLACEMENTS

def skip_chars(src, pos, chars):
    while pos < len(src) and src[pos] in chars:
        pos += 1
    return pos

TOML_WS = " \t\n"
TOML_WS_AND_NEWLINE = TOML_WS + "\r\f"

def test_error_case_invalid_escape():
    src = 'Hello\\x'
    with pytest.raises(ValueError):
        parse_basic_str_escape(src, Pos(0))
