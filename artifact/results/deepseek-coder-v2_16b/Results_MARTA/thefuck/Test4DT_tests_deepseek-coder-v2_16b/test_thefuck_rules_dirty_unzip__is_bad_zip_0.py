
import pytest
import zipfile
from thefuck.rules.dirty_unzip import _is_bad_zip


def test_invalid_zip_file():
    # Provide a path to an invalid or non-existent ZIP file
    zip_file = 'nonexistent_file.zip'
    assert _is_bad_zip(zip_file) is False, "Expected False for an invalid or non-existent ZIP file"