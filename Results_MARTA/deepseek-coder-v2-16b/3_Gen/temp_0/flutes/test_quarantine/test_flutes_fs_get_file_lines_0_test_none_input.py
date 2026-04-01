
import subprocess
from pathlib import Path
import pytest

def get_file_lines(path: PathType) -> int:
    r"""Get number of lines in text file.
    """
    return int(subprocess.check_output(['wc', '-l', str(path)]).split()[0].decode('utf-8'))

def test_none_input():
    # Test when input is None
    with pytest.raises(TypeError):
        get_file_lines(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_fs_get_file_lines_0_test_none_input
flutes/Test4DT_tests/test_flutes_fs_get_file_lines_0_test_none_input.py:6:25: E0602: Undefined variable 'PathType' (undefined-variable)


"""