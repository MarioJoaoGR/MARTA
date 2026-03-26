
import os
import sys
from unittest.mock import patch
import pytest

def exists_case_sensitive(path: str) -> bool:
    """Returns if the given path exists and also matches the case on Windows.

    When finding files that can be imported, it is important for the cases to match because while
    file os.path.exists("module.py") and os.path.exists("MODULE.py") both return True on Windows,
    Python can only import using the case of the real file.
    """
    result = os.path.exists(path)
    if result and (sys.platform.startswith("win") or sys.platform == "darwin"):  # pragma: no cover
        directory, basename = os.path.split(path)
        result = basename in os.listdir(directory)
    return result

@pytest.fixture
def create_temp_file():
    temp_file_name = "testfile.txt"
    temp_file_path = os.path.join(os.getcwd(), temp_file_name)
    with open(temp_file_path, 'w') as f:
        f.write("Test content")
    yield temp_file_path
    os.remove(temp_file_path)

def test_valid_path_exists(create_temp_file):
    assert exists_case_sensitive(create_temp_file) == True
