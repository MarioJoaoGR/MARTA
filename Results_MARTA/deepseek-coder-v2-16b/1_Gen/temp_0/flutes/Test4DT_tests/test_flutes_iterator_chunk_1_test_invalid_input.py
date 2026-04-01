
import pytest
from flutes.iterator import chunk

def test_invalid_input():
    with pytest.raises(ValueError):
        list(chunk(0, range(10)))
