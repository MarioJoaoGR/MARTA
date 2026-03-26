
from typing import Optional, Tuple

import pytest

from isort._vendored.tomli._parser import (TOML_WS, Key, Pos, parse_key,
                                           skip_chars)


def test_invalid_input_none():
    src = None  # Invalid input as it should be a string
    pos = Pos(0)
    
    with pytest.raises(TypeError):  # Expecting a TypeError since parse_key does not accept None
        new_pos, parsed_key = parse_key(src, pos)
