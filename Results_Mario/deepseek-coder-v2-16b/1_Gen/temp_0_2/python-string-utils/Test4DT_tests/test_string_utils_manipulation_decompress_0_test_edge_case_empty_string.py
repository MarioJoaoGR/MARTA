
import pytest
from string_utils.manipulation import decompress

def test_edge_case_empty_string():
    with pytest.raises(ValueError):
        decompress("")
