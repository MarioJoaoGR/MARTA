
from isort._vendored.tomli._parser import parse_key, Pos, TOML_WS, BARE_KEY_CHARS, Key, parse_key_part, skip_chars, parse_literal_str, parse_one_line_basic_str, TOMLDecodeError
import pytest

def test_edge_case_empty_string():
    src = ''
    pos = Pos(0)
    with pytest.raises(TOMLDecodeError):
        _, _ = parse_key(src, pos)
