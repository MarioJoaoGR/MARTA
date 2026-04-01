
import pytest
from pathlib import Path
import shutil
from flutes.fs import copy_tree

@pytest.mark.parametrize("src, dst, overwrite", [
    (Path("/nonexistent/source"), Path("/path/to/destination"), False),
    (Path("/path/to/source"), Path("/nonexistent/destination"), False),
    (Path("/path/to/source"), Path("/path/to/destination"), True)
])
def test_invalid_inputs(src, dst, overwrite):
    with pytest.raises(FileNotFoundError):
        copy_tree(src, dst, overwrite)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

flutes/Test4DT_tests/test_flutes_fs_copy_tree_0_test_invalid_inputs.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_____________________ test_invalid_inputs[src0-dst0-False] _____________________

src = PosixPath('/nonexistent/source'), dst = PosixPath('/path/to/destination')
overwrite = False

    @pytest.mark.parametrize("src, dst, overwrite", [
        (Path("/nonexistent/source"), Path("/path/to/destination"), False),
        (Path("/path/to/source"), Path("/nonexistent/destination"), False),
        (Path("/path/to/source"), Path("/path/to/destination"), True)
    ])
    def test_invalid_inputs(src, dst, overwrite):
        with pytest.raises(FileNotFoundError):
>           copy_tree(src, dst, overwrite)

flutes/Test4DT_tests/test_flutes_fs_copy_tree_0_test_invalid_inputs.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/fs.py:118: in copy_tree
    os.makedirs(dst, exist_ok=True)
<frozen os>:215: in makedirs
    ???
<frozen os>:215: in makedirs
    ???
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

name = '/path', mode = 511, exist_ok = True

>   ???
E   OSError: [Errno 30] Read-only file system: '/path'

<frozen os>:225: OSError
_____________________ test_invalid_inputs[src1-dst1-False] _____________________

src = PosixPath('/path/to/source'), dst = PosixPath('/nonexistent/destination')
overwrite = False

    @pytest.mark.parametrize("src, dst, overwrite", [
        (Path("/nonexistent/source"), Path("/path/to/destination"), False),
        (Path("/path/to/source"), Path("/nonexistent/destination"), False),
        (Path("/path/to/source"), Path("/path/to/destination"), True)
    ])
    def test_invalid_inputs(src, dst, overwrite):
        with pytest.raises(FileNotFoundError):
>           copy_tree(src, dst, overwrite)

flutes/Test4DT_tests/test_flutes_fs_copy_tree_0_test_invalid_inputs.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/fs.py:118: in copy_tree
    os.makedirs(dst, exist_ok=True)
<frozen os>:215: in makedirs
    ???
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

name = '/nonexistent', mode = 511, exist_ok = True

>   ???
E   OSError: [Errno 30] Read-only file system: '/nonexistent'

<frozen os>:225: OSError
_____________________ test_invalid_inputs[src2-dst2-True] ______________________

src = PosixPath('/path/to/source'), dst = PosixPath('/path/to/destination')
overwrite = True

    @pytest.mark.parametrize("src, dst, overwrite", [
        (Path("/nonexistent/source"), Path("/path/to/destination"), False),
        (Path("/path/to/source"), Path("/nonexistent/destination"), False),
        (Path("/path/to/source"), Path("/path/to/destination"), True)
    ])
    def test_invalid_inputs(src, dst, overwrite):
        with pytest.raises(FileNotFoundError):
>           copy_tree(src, dst, overwrite)

flutes/Test4DT_tests/test_flutes_fs_copy_tree_0_test_invalid_inputs.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/fs.py:118: in copy_tree
    os.makedirs(dst, exist_ok=True)
<frozen os>:215: in makedirs
    ???
<frozen os>:215: in makedirs
    ???
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

name = '/path', mode = 511, exist_ok = True

>   ???
E   OSError: [Errno 30] Read-only file system: '/path'

<frozen os>:225: OSError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_copy_tree_0_test_invalid_inputs.py::test_invalid_inputs[src0-dst0-False]
FAILED flutes/Test4DT_tests/test_flutes_fs_copy_tree_0_test_invalid_inputs.py::test_invalid_inputs[src1-dst1-False]
FAILED flutes/Test4DT_tests/test_flutes_fs_copy_tree_0_test_invalid_inputs.py::test_invalid_inputs[src2-dst2-True]
============================== 3 failed in 0.11s ===============================
"""