
import pytest
from isort._vendored.tomli._parser import parse_key_part, suffixed_err
from isort._vendored.tomli._parser import BARE_KEY_CHARS, Pos, skip_chars

def test_invalid_initial_char():
    # Test case for invalid initial character for a key part
    src = "!key"
    pos = Pos(0)
    with pytest.raises(ValueError) as exc_info:
        new_pos, parsed_key = parse_key_part(src, pos)
    
    assert str(exc_info.value) == "Invalid initial character for a key part (at line 1, column 1)", f"Unexpected error message: {str(exc_info.value)}"
