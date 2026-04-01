
import pytest
from string_utils.manipulation import asciify

def test_edge_case_none():
    with pytest.raises(TypeError):
        asciify(None)
