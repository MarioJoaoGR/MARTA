
import pytest

def is_zip_file(value):
    """Return True if value is a zip file."""
    return value.lower().endswith('.zip')

def test_is_zip_file_basic():
    assert is_zip_file('example.zip') == True
    assert is_zip_file('archive.ZIP') == True
