
import pytest
from isort.exceptions import UnsupportedEncoding
from pathlib import Path

def test_invalid_input():
    with pytest.raises(UnsupportedEncoding) as excinfo:
        raise UnsupportedEncoding("non_existent_file.txt")
    
    assert str(excinfo.value) == "Unknown or unsupported encoding in non_existent_file.txt"
