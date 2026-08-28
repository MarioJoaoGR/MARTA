
import pytest
from pathlib import Path
from isort.exceptions import UnsupportedEncoding

def test_valid_string_filename():
    filename = 'example.txt'
    with pytest.raises(UnsupportedEncoding) as excinfo:
        raise UnsupportedEncoding(filename)
    assert str(excinfo.value) == f"Unknown or unsupported encoding in {filename}"
    assert excinfo.value.filename == filename

def test_valid_pathlib_filename():
    filename = Path('data/sample_file.txt')
    with pytest.raises(UnsupportedEncoding) as excinfo:
        raise UnsupportedEncoding(filename)
    assert str(excinfo.value) == f"Unknown or unsupported encoding in {filename}"
    assert excinfo.value.filename == filename

def test_invalid_none_filename():
    filename = None
    with pytest.raises(UnsupportedEncoding) as excinfo:
        raise UnsupportedEncoding(filename)
    assert str(excinfo.value) == f"Unknown or unsupported encoding in {filename}"
    assert excinfo.value.filename == filename
