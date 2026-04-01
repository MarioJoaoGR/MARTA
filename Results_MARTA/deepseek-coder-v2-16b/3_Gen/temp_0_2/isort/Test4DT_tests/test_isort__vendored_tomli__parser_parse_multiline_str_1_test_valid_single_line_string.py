
import pytest
from isort._vendored.tomli._parser import parse_multiline_str, TOMLDecodeError

def test_valid_single_line_string():
    src = 'Hello "world"'
    pos = 0
    with pytest.raises(TOMLDecodeError) as excinfo:
        new_pos, parsed_str = parse_multiline_str(src, pos, literal=False)
    assert str(excinfo.value) == "Unterminated string (at end of document)"
