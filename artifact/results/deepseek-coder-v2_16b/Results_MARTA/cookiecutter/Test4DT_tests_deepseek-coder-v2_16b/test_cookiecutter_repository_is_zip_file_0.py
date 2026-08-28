
import pytest
from cookiecutter.repository import is_zip_file

# Test for a valid zip file
def test_valid_zip_file():
    value = 'example.zip'
    assert is_zip_file(value) == True

# Test for an invalid extension (not ending with '.zip')
def test_invalid_extension():
    value = 'archive.txt'
    assert is_zip_file(value) == False

# Test for case-insensitivity by providing a file name with uppercase extension
def test_case_insensitive():
    value = 'ExampleFile.ZIP'
    assert is_zip_file(value) == True
