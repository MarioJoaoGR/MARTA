
import pytest
from pathlib import Path
import os
from typing import Iterator, Union

# Assuming the function is defined in a module named 'scandir_module'
from scandir_module import scandir

@pytest.fixture(params=[Path("invalid_path"), "invalid_path"])
def invalid_paths(request):
    return request.param

def test_invalid_input(invalid_paths):
    with pytest.raises(FileNotFoundError):
        list(scandir(invalid_paths))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_fs_scandir_2_test_invalid_input
flutes/Test4DT_tests/test_flutes_fs_scandir_2_test_invalid_input.py:8:0: E0401: Unable to import 'scandir_module' (import-error)


"""