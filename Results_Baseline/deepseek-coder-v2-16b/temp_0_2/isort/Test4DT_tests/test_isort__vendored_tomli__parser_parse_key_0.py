
from typing import Tuple

import pytest

from isort._vendored.tomli._parser import parse_key

# Assuming the types Key and Pos are defined elsewhere in the module or imported from appropriate libraries
Key = Tuple[str, ...]
Pos = int
TOML_WS = str  # Placeholder for TOML whitespace characters; adjust based on actual definition
BARE_KEY_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0987654321_"

def test_parse_basic_key():
    src = "example_key = 'Hello, World!'\\nprint(example_key)"
    pos = 0
    new_pos, key = parse_key(src, pos)
    assert key == ('example_key',)