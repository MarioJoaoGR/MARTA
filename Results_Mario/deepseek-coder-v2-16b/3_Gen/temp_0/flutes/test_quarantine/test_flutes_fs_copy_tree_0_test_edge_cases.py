
import os
import shutil
from pathlib import Path
from flutes.fs import copy_tree

def test_copy_tree():
    src = Path("test_source")
    dst = Path("test_destination")
    
    # Create source directory and files
    os.makedirs(src, exist_ok=True)
    (src / "file1").write_text("content1")
    (src / "dir1" / "file2").write_text("content2")
    
    # Copy tree should not overwrite existing files by default
    copy_tree(src, dst)
    assert os.path.exists(dst / "file1")
    assert not os.path.exists(dst / "dir1" / "file2")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_fs_copy_tree_0_test_edge_cases.py F     [100%]

=================================== FAILURES ===================================
________________________________ test_copy_tree ________________________________

    def test_copy_tree():
        src = Path("test_source")
        dst = Path("test_destination")
    
        # Create source directory and files
        os.makedirs(src, exist_ok=True)
        (src / "file1").write_text("content1")
        (src / "dir1" / "file2").write_text("content2")
    
        # Copy tree should not overwrite existing files by default
        copy_tree(src, dst)
        assert os.path.exists(dst / "file1")
>       assert not os.path.exists(dst / "dir1" / "file2")
E       AssertionError: assert not True
E        +  where True = <function exists at 0x7ff48953b560>(((PosixPath('test_destination') / 'dir1') / 'file2'))
E        +    where <function exists at 0x7ff48953b560> = <module 'posixpath' (frozen)>.exists
E        +      where <module 'posixpath' (frozen)> = os.path

flutes/Test4DT_tests/test_flutes_fs_copy_tree_0_test_edge_cases.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_copy_tree_0_test_edge_cases.py::test_copy_tree
============================== 1 failed in 0.14s ===============================
"""