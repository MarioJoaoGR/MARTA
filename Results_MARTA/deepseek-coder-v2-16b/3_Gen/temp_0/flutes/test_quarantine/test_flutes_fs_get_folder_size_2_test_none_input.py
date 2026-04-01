
import subprocess
from unittest.mock import patch
import pytest

def get_folder_size(path: PathType) -> int:
    """Get disk usage of given path in bytes."""
    return int(subprocess.check_output(['du', '-s', str(path)],
                                       env={"BLOCKSIZE": "512"}).split()[0].decode('utf-8')) * 512

def test_none_input():
    with pytest.raises(TypeError) as excinfo:
        get_folder_size(None)
    assert str(excinfo.value) == "get_folder_size() missing 1 required positional argument: 'path'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_fs_get_folder_size_2_test_none_input
flutes/Test4DT_tests/test_flutes_fs_get_folder_size_2_test_none_input.py:6:26: E0602: Undefined variable 'PathType' (undefined-variable)

"""