
import pytest
from flutes.iterator import take

def test_negative_n():
    with pytest.raises(ValueError):
        list(take(-1, range(10)))
