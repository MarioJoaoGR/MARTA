
import pytest
from flutes.io import reverse_open, PathType

def test_invalid_input():
    with pytest.raises(FileNotFoundError):
        reverse_open('non_existent_file.txt')
