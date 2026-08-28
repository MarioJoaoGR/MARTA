
import pytest
from cookiecutter.repository import is_zip_file

# Test for valid zip file names
def test_valid_input_happy_path():
    assert is_zip_file("example.zip") == True
    assert is_zip_file("ExampleFile.ZIP") == True
    assert is_zip_file("/path/to/archive.zip") == True

# Test for invalid file extensions
def test_invalid_extension():
    assert is_zip_file("example.txt") == False
    assert is_zip_file("archive.zipx") == False
    assert is_zip_file("ExampleFile.zippy") == False

# Test handling of None input
def test_none_input():
    with pytest.raises(AttributeError):
        is_zip_file(None)
