
import pytest
from isort.exceptions import UnsupportedEncoding

def test_edge_case_none():
    filename = None
    with pytest.raises(UnsupportedEncoding):
        raise UnsupportedEncoding(filename)
