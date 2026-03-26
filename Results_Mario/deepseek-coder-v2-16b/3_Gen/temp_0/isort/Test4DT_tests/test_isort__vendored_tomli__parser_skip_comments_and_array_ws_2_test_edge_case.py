
import pytest

from isort._vendored.tomli._parser import (TOML_WS_AND_NEWLINE,
                                           skip_comments_and_array_ws)


def test_edge_case():
    src = None
    pos = 0
    
    with pytest.raises(TypeError):
        skip_comments_and_array_ws(src, pos)
