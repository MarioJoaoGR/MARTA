# Module: cookiecutter.repository
import pytest
from cookiecutter.repository import is_zip_file

# Test case 1: Valid zip file extension
def test_is_zip_file_valid_zip():
    assert is_zip_file("example.zip") == True

# Test case 2: Case insensitive check with uppercase extension
def test_is_zip_file_case_insensitive():
    assert is_zip_file("Example.ZIP") == True

# Test case 3: File without zip extension
def test_is_zip_file_no_zip_extension():
    assert is_zip_file("example.txt") == False

# Test case 4: File with tar.gz extension
def test_is_zip_file_tar_gz_extension():
    assert is_zip_file("archive.tar.gz") == False
