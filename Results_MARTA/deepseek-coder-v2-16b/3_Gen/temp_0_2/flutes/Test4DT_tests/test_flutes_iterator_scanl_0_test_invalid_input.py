
import pytest
from flutes.iterator import scanl

def test_invalid_input():
    with pytest.raises(TypeError):
        list(scanl(lambda x, y: x + y, [1, 2, 3], initial=0, extra=1))
