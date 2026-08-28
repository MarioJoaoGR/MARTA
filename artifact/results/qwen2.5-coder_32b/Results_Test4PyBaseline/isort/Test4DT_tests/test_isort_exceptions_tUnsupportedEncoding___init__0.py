
import pytest
from pathlib import Path
from isort.exceptions import UnsupportedEncoding

def test_unsupported_encoding_with_string_filename():
    with pytest.raises(UnsupportedEncoding) as excinfo:
        raise UnsupportedEncoding("example.py")
    assert str(excinfo.value) == "Unknown or unsupported encoding in example.py"
    assert excinfo.value.filename == "example.py"

def test_unsupported_encoding_with_path_object():
    file_path = Path("example.py")
    with pytest.raises(UnsupportedEncoding) as excinfo:
        raise UnsupportedEncoding(file_path)
    assert str(excinfo.value) == f"Unknown or unsupported encoding in {file_path}"
    assert excinfo.value.filename == file_path

def test_unsupported_encoding_with_empty_string():
    with pytest.raises(UnsupportedEncoding) as excinfo:
        raise UnsupportedEncoding("")
    assert str(excinfo.value) == "Unknown or unsupported encoding in "