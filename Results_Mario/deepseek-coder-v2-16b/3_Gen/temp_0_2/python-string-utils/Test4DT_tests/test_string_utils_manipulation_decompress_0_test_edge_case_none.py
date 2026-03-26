
import pytest
from string_utils.manipulation import decompress

def test_edge_case_none():
    with pytest.raises(TypeError):
        decompress(None)
