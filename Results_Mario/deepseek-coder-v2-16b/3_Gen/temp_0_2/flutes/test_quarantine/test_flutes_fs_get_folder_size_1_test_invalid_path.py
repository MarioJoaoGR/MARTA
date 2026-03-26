
import subprocess
from unittest.mock import patch, MagicMock
import pytest
from pathlib import Path

def get_folder_size(path: PathType) -> int:
    """Get disk usage of given path in bytes."""
    return int(subprocess.check_output(['du', '-s', str(path)], env={"BLOCKSIZE": "512"}).split()[0].decode('utf-8')) * 512

def test_invalid_path():
    with pytest.raises(FileNotFoundError):
        get_folder_size('non/existent/path')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_fs_get_folder_size_1_test_invalid_path
flutes/Test4DT_tests/test_flutes_fs_get_folder_size_1_test_invalid_path.py:7:26: E0602: Undefined variable 'PathType' (undefined-variable)


"""