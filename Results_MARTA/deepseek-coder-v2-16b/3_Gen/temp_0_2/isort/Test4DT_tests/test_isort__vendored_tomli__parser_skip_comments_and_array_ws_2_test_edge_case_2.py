
import pytest
from isort._vendored.tomli._parser import skip_comments_and_array_ws, TOML_WS_AND_NEWLINE

def test_edge_case_2():
    src = ''
    pos = 0
    result = skip_comments_and_array_ws(src, pos)
    assert result == pos
