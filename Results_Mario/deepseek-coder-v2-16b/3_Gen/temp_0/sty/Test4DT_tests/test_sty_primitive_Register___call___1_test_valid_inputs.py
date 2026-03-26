
import pytest
from sty import primitive

@pytest.fixture
def reg():
    return primitive.Register()

def test_valid_inputs(reg):
    # Test setting fg to an 8-bit color code
    assert reg(fg=42) == ""
    
    # Test setting bg to a 24-bit RGB color
    with pytest.raises(AssertionError):
        assert reg(bg=(102, 49, 42)) == (102, 49, 42)
