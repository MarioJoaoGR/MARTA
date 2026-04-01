
import pytest
from flutes.io import progress_open
import io

def test_invalid_inputs():
    with pytest.raises(ValueError):
        progress_open("test.txt", mode="w")  # Unsupported write mode
