
import pytest
from isort._vendored.tomli._parser import skip_comment, TOMLDecodeError

def test_no_comment_found():
    src = 'abcdef'
    pos = 0
    new_pos = skip_comment(src, pos)
    assert new_pos == 0
