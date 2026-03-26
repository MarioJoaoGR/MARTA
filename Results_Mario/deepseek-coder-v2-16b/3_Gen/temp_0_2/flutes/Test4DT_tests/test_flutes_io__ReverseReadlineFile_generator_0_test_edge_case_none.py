
import pytest
from flutes.io import _ReverseReadlineFile

def test_edge_case_none():
    with pytest.raises(TypeError):
        reverse_readline = _ReverseReadlineFile(None, None)
        list(reverse_readline)
