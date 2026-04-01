
import pytest
from pathlib import Path
import io
from flutes.io import reverse_open

def test_invalid_input():
    with pytest.raises(ValueError):
        # Test when buffer_size is less than the minimum allowed value
        reverse_open('nonexistentfile.txt', buffer_size=-1)
