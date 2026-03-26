
from typing import Tuple

import pytest

from isort._vendored.tomli._parser import Key, Pos, parse_key

# Assuming TOML_WS and skip_chars are defined elsewhere in the module
TOML_WS = " \t\n"  # Example whitespace characters for skipping

def test_parse_key_typical():
    src = "example.key1.key2"
    pos = 0
    new_pos, key = parse_key(src, pos)
    assert new_pos == len("example.key1.key2")