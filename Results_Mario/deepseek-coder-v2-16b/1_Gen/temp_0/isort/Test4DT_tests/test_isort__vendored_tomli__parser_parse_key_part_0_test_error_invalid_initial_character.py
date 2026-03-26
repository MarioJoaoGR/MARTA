
import pytest
from isort._vendored.tomli._parser import parse_key_part, BARE_KEY_CHARS, skip_chars

def test_error_invalid_initial_character():
    with pytest.raises(ValueError) as excinfo:
        src = "!example"
        pos = 0
        parse_key_part(src, pos)
    assert str(excinfo.value) == 'Invalid initial character for a key part (at line 1, column 1)'
