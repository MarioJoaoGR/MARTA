
import pytest
from flutes.iterator import take

def test_none_input():
    with pytest.raises(ValueError):
        list(take(-1, []))
