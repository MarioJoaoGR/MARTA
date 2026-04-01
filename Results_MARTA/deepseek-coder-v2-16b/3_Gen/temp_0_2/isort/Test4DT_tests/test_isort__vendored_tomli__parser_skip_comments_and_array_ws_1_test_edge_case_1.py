
import pytest
from isort._vendored.tomli._parser import skip_comments_and_array_ws, TOML_WS_AND_NEWLINE, Pos

def test_edge_case_1():
    src = None
    pos = 0
    with pytest.raises(TypeError):
        result = skip_comments_and_array_ws(src, pos)
