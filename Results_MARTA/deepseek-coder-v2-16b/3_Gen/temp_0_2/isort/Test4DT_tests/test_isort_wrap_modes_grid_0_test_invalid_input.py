
import pytest
from isort.wrap_modes import grid

def test_invalid_input():
    with pytest.raises(KeyError):
        grid()  # This should raise a KeyError because the 'imports' key is not provided in the interface dictionary.
