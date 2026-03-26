
import pytest
from flutes.iterator import scanr

def test_invalid_input():
    with pytest.raises(TypeError):
        # Test when 'initial' is provided as a positional argument
        scanr(lambda x, y: x + y, [1, 2, 3], initial=0)
