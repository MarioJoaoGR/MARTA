
import pytest
from typing import Tuple, Optional
from isort._vendored.tomli._parser import Pos, Key, TOML_WS, parse_key, skip_chars, parse_key_part

def test_error_case_none_input():
    with pytest.raises(TypeError):
        pos, parsed_key = parse_key(None, Pos(0))
