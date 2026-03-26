
import os
import shutil
from pathlib import Path
from flutes.fs import copy_tree  # Assuming the function is defined in a module named fs within the flutes package

def test_edge_cases():
    # Create a temporary directory for testing
    temp_dir = Path('temp_test_dir')
    src_dir = temp_dir / 'src'
    dst_dir = temp_dir / 'dst'

    # Create source directory with some files and subdirectories
    os.makedirs(src_dir)
    (src_dir / 'file1').touch()
    (src_dir / 'subdir').mkdir()
    (src_dir / 'subdir' / 'file2').touch()

    # Copy tree should not overwrite existing files if overwrite=False
    shutil.copytree(str(src_dir), str(dst_dir))
    assert len(list(dst_dir.glob('*'))) == 2, "Expected two items in dst_dir"

    # Now test with overwrite=True
    copy_tree(str(src_dir), str(dst_dir), overwrite=True)
    assert len(list(dst_dir.glob('*'))) == 3, "Expected three items in dst_dir after overwriting"

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

flutes/Test4DT_tests/test_flutes_fs_copy_tree_1_test_edge_cases.py F     [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Create a temporary directory for testing
        temp_dir = Path('temp_test_dir')
        src_dir = temp_dir / 'src'
        dst_dir = temp_dir / 'dst'
    
        # Create source directory with some files and subdirectories
>       os.makedirs(src_dir)

flutes/Test4DT_tests/test_flutes_fs_copy_tree_1_test_edge_cases.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

name = PosixPath('temp_test_dir/src'), mode = 511, exist_ok = False

>   ???
E   FileExistsError: [Errno 17] File exists: 'temp_test_dir/src'

<frozen os>:225: FileExistsError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_copy_tree_1_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.09s ===============================
"""