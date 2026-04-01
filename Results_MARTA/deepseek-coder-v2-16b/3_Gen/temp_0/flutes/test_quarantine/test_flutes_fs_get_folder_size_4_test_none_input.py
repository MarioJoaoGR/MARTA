
import subprocess
from pathlib import Path
import pytest

@pytest.mark.skip(reason="This test is not yet implemented")
def test_none_input():
    with pytest.raises(TypeError):
        get_folder_size(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_fs_get_folder_size_4_test_none_input
flutes/Test4DT_tests/test_flutes_fs_get_folder_size_4_test_none_input.py:9:8: E0602: Undefined variable 'get_folder_size' (undefined-variable)

"""