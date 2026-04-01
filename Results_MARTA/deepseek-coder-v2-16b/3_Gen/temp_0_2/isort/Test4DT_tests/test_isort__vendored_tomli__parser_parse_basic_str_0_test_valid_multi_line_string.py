
import pytest
from isort._vendored.tomli._parser import parse_basic_str, TOMLDecodeError

def test_valid_multi_line_string():
    src = 'Hello \\"""world\\"""'
    pos = 0
    with pytest.raises(TOMLDecodeError) as excinfo:
        new_pos, parsed_str = parse_basic_str(src, pos, multiline=True)
    assert str(excinfo.value) == "Unterminated string (at end of document)"
