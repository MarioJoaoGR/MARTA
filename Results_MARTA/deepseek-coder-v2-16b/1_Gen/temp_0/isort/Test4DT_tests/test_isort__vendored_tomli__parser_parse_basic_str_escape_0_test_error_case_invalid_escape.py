
import pytest
from isort._vendored.tomli._parser import parse_basic_str_escape, Pos, TOML_WS, skip_chars, suffixed_err

def test_error_case_invalid_escape():
    src = 'Hello\\x'
    pos = 0
    with pytest.raises(ValueError):
        parse_basic_str_escape(src, Pos(pos))
