
import pytest
import zipfile
from unittest.mock import patch, MagicMock

def _is_bad_zip(file):
    try:
        with zipfile.ZipFile(file, 'r') as archive:
            return len(archive.namelist()) > 1
    except Exception:
        return False

# Test for a valid ZIP file with multiple entries
def test_valid_zip_with_multiple_entries():
    # Create a temporary ZIP file with multiple entries
    with zipfile.ZipFile('good_archive.zip', 'w') as archive:
        archive.writestr("entry1.txt", "content1")
        archive.writestr("entry2.txt", "content2")
    
    # Test the function with the created ZIP file
    result = _is_bad_zip('good_archive.zip')
    assert result is True, "Expected True for a valid ZIP with multiple entries"

# Test for an invalid or non-existent file path
def test_invalid_file():
    # Test the function with a non-existent file path
    result = _is_bad_zip('nonexistent_file.zip')
    assert result is False, "Expected False for a non-existent file"

# Test for providing a non-ZIP file
def test_non_zip_file():
    # Create a temporary text file instead of a ZIP file
    with open('bad_archive.txt', 'w') as file:
        file.write("This is not a ZIP file")
    
    # Test the function with the created text file
    result = _is_bad_zip('bad_archive.txt')
    assert result is False, "Expected False for a non-ZIP file"
