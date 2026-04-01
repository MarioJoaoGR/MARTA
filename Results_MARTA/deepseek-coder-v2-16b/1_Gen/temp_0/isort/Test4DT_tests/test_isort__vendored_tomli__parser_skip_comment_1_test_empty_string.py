
import pytest
from isort._vendored.tomli._parser import skip_comment

def test_empty_string():
    src = ""
    pos = 0
    new_pos = skip_comment(src, pos)
    assert new_pos == pos
