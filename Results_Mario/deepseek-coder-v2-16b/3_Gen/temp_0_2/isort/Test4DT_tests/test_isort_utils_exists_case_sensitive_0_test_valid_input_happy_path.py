
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

@pytest.mark.skipif(sys.platform != 'win32', reason="This test is for Windows only")
def test_valid_input_happy_path():
    with patch('os.path.exists') as mock_exists:
        with patch('os.listdir') as mock_listdir:
            mock_exists.return_value = True
            mock_listdir.return_value = ['module.py']
            assert exists_case_sensitive("C:\\path\\to\\module.py") == True
