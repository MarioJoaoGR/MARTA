
import pytest
from string_utils.manipulation import prettify

def test_edge_case_none():
    with pytest.raises(TypeError):
        prettify(None)
