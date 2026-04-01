
from isort.exceptions import UnsupportedEncoding
import pytest

def test_invalid_input():
    with pytest.raises(UnsupportedEncoding) as excinfo:
        raise UnsupportedEncoding("example_file.txt")
    
    assert str(excinfo.value) == "Unknown or unsupported encoding in example_file.txt"
