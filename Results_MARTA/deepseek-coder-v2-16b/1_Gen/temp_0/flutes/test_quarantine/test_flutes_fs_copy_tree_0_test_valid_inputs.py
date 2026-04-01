
import os
import shutil
from pathlib import Path
from flutes.fs import copy_tree  # Assuming the function is defined in a module named fs within the flutes package

def test_valid_inputs():
    src = Path("test_source")
    dst = Path("test_destination")
    
    # Create source directory and files
    os.makedirs(src, exist_ok=True)
    (src / "file1").touch()
    (src / "subdir").mkdir()
    (src / "subdir" / "file2").touch()
    
    # Copy tree should not overwrite existing files by default
    copy_tree(src, dst)
    assert os.path.exists(dst / "file1")
    assert os.path.isdir(dst / "subdir")
    assert os.path.exists(dst / "subdir" / "file2")
    
    # Copy tree should overwrite existing files if overwrite=True
    copy_tree(src, dst, overwrite=True)
    assert not os.path.exists(dst / "file1")  # Should be overwritten

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_fs_copy_tree_0_test_valid_inputs.py F   [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        src = Path("test_source")
        dst = Path("test_destination")
    
        # Create source directory and files
        os.makedirs(src, exist_ok=True)
        (src / "file1").touch()
>       (src / "subdir").mkdir()

flutes/Test4DT_tests/test_flutes_fs_copy_tree_0_test_valid_inputs.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = PosixPath('test_source/subdir'), mode = 511, parents = False
exist_ok = False

    def mkdir(self, mode=0o777, parents=False, exist_ok=False):
        """
        Create a new directory at this given path.
        """
        try:
>           os.mkdir(self, mode)
E           FileExistsError: [Errno 17] File exists: 'test_source/subdir'

/usr/local/lib/python3.11/pathlib.py:1116: FileExistsError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_copy_tree_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.10s ===============================
"""