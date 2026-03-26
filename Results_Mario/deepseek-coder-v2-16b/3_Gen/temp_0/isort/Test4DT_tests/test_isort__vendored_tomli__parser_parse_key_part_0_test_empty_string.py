
import pytest
from isort._vendored.tomli._parser import parse_key_part, suffixed_err
from isort._vendored.tomli._parser import Pos

def test_empty_string():
    src = ''
    pos = Pos(0)
    
    with pytest.raises(ValueError):
        parse_key_part(src, pos)
