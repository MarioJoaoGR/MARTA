
import pytest
from isort.exceptions import UnsupportedEncoding

def test_edge_case_none():
    with pytest.raises(UnsupportedEncoding) as exc_info:
        raise UnsupportedEncoding(None)
    
    assert str(exc_info.value) == "Unknown or unsupported encoding in None"
