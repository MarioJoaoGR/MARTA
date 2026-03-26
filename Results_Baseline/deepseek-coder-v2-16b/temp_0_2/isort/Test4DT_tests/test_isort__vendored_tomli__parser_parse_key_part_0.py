
from typing import Optional, Tuple

import pytest

from isort._vendored.tomli._parser import (BARE_KEY_CHARS, parse_key_part,
                                           parse_literal_str,
                                           parse_one_line_basic_str,
                                           skip_chars, suffixed_err)

# Test cases for parse_key_part function

def test_parse_bare_key():
    src = "let x = 42"
    pos = 0
    new_pos, key_part = parse_key_part(src, pos)
    assert key_part == 'let'