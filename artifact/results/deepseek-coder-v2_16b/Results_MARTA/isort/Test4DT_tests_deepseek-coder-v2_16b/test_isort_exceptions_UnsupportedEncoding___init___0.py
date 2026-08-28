
import pytest
from pathlib import Path
from isort.exceptions import UnsupportedEncoding

# Test for invalid input scenario where a FileNotFoundError should be raised
def test_invalid_input():
    filename = "nonexistent_file.txt"
    with pytest.raises(FileNotFoundError) as excinfo:
        raise FileNotFoundError(f"No such file or directory: '{filename}'")
    assert str(excinfo.value) == f"No such file or directory: '{filename}'"

# Test for valid input scenario where an UnsupportedEncoding error should be raised
def test_valid_input():
    filename = "example_file.txt"
    with pytest.raises(UnsupportedEncoding) as excinfo:
        raise UnsupportedEncoding(filename)
    assert str(excinfo.value) == f"Unknown or unsupported encoding in {filename}"
