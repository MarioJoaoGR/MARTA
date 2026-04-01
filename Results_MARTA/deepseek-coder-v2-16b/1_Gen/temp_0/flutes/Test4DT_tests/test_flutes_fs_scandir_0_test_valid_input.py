
import pytest
from pathlib import Path
from flutes.fs import scandir

def test_valid_input():
    # Test with a string representing a directory path
    test_dir_path = "/some/directory"
    with pytest.raises(FileNotFoundError):
        result = list(scandir(test_dir_path))
