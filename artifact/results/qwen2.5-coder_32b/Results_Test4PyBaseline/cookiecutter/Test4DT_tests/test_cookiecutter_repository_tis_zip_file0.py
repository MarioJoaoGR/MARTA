# Module: cookiecutter.repository
import pytest
from cookiecutter.repository import is_zip_file

def test_is_zip_file_with_lowercase_extension():
    assert is_zip_file('example.zip') == True, "Should recognize lowercase .zip extension"

def test_is_zip_file_with_uppercase_extension():
    assert is_zip_file('archive.ZIP') == True, "Should recognize uppercase .ZIP extension"

def test_is_zip_file_without_extension():
    assert is_zip_file('data') == False, "Should return False for filenames without an extension"

def test_is_zip_file_with_different_extension():
    assert is_zip_file('document.pdf') == False, "Should return False for different file extensions"

def test_is_zip_file_with_path():
    assert is_zip_file('/path/to/file.zip') == True, "Should recognize .zip extension in a path"

def test_is_zip_file_with_url():
    assert is_zip_file('http://example.com/resource.ZIP') == True, "Should recognize .ZIP extension in a URL"

def test_is_zip_file_empty_string():
    assert is_zip_file('') == False, "Should return False for an empty string"

def test_is_zip_file_only_dot():
    assert is_zip_file('.') == False, "Should return False for a single dot"

def test_is_zip_file_with_partial_extension():
    assert is_zip_file('.zip') == True, "Should recognize .zip as a valid extension"
    assert is_zip_file('.ZIP') == True, "Should recognize .ZIP as a valid extension"
