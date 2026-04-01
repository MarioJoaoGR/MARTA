
import pytest
from isort.exceptions import UnsupportedEncoding

def test_invalid_input():
    filename = 12345
    with pytest.raises(UnsupportedEncoding):
        raise UnsupportedEncoding(filename)
