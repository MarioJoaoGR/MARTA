
import pytest

from isort.exceptions import UnsupportedEncoding


def test_valid_input():
    filename = 'example_file.txt'
    with pytest.raises(UnsupportedEncoding) as exc_info:
        raise UnsupportedEncoding(filename)
    assert str(exc_info.value) == f"Unknown or unsupported encoding in {filename}"
