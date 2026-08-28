# Module: isort.exceptions
# test_isort_exceptions.py
from isort.exceptions import UnsupportedEncoding
import pytest
from pathlib import Path

def test_unsupported_encoding_basic():
    with pytest.raises(UnsupportedEncoding) as excinfo:
        raise UnsupportedEncoding("example_file.txt")
    assert str(excinfo.value) == "Unknown or unsupported encoding in example_file.txt"

def test_unsupported_encoding_with_pathlib():
    filename = Path("example_file.txt")
    with pytest.raises(UnsupportedEncoding) as excinfo:
        raise UnsupportedEncoding(filename)
    assert str(excinfo.value) == f"Unknown or unsupported encoding in {filename}"
