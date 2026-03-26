
from flutes.iterator import take  # Importing the take function from the iterator module
import pytest

def test_negative_input():
    with pytest.raises(ValueError):
        list(take(-1, range(5)))
