
import pytest
from flutes.fs import readable_size

def test_edge_cases():
    # Test None value
    with pytest.raises(TypeError):
        assert readable_size(None) is None, "Expected None to be returned for None input"
