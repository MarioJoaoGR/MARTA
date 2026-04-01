
import pytest
from isort._vendored.tomli._parser import skip_comment, TOMLDecodeError

def test_none_input():
    src = None
    pos = 0
    with pytest.raises(TypeError):
        new_pos = skip_comment(src, pos)
