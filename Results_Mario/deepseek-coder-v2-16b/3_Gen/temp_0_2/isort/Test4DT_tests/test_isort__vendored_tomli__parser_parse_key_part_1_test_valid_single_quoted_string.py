
import pytest
from typing import Tuple, Optional
from isort._vendored.tomli._parser import BARE_KEY_CHARS, parse_key_part, skip_chars, suffixed_err

def test_valid_single_quoted_string():
    src = "'hello world'"
    pos = 0
    new_pos, lit_str = parse_key_part(src, pos)
    assert new_pos == len("'hello world'")
    assert lit_str == "hello world"
