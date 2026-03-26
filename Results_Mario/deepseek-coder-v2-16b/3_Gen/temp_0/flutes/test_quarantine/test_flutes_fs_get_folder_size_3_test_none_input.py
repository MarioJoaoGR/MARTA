
import pytest
from pathlib import Path
import subprocess

def get_folder_size(path: PathType) -> int:
    r"""Get disk usage of given path in bytes."""
    if path is None:
        raise TypeError("Path must be a valid path, not None")
    return int(subprocess.check_output(['du', '-bs', str(path)]).split()[0].decode('utf-8'))

def test_none_input():
    with pytest.raises(TypeError):
        assert get_folder_size(None) == 0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_fs_get_folder_size_3_test_none_input
flutes/Test4DT_tests/test_flutes_fs_get_folder_size_3_test_none_input.py:6:26: E0602: Undefined variable 'PathType' (undefined-variable)

"""