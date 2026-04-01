
import os
import sys
import pytest
from unittest.mock import patch

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

@pytest.mark.skipif(not sys.platform.startswith("win"), reason="This test is for Windows only")
def test_valid_path_exists():
    # Use a known existing file path that matches its case on Windows
    valid_path = "C:\\Windows\\System32\\cmd.exe"  # Example of a valid path on Windows
    
    with patch('os.listdir') as mock_listdir:
        mock_listdir.return_value = ["cmd.exe"]  # Mock the listdir to return expected value
        assert exists_case_sensitive(valid_path) == True
