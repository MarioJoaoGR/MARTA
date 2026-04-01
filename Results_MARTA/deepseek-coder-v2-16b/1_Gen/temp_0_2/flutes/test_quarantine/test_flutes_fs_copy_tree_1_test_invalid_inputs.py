
import os
import shutil
from flutes.fs import copy_tree

def test_invalid_inputs():
    # Test invalid source path
    try:
        copy_tree("invalid_source", "destination_dir")
    except FileNotFoundError as e:
        assert str(e) == "No such file or directory: 'invalid_source'"

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

flutes/Test4DT_tests/test_flutes_fs_copy_tree_1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test invalid source path
        try:
>           copy_tree("invalid_source", "destination_dir")

flutes/Test4DT_tests/test_flutes_fs_copy_tree_1_test_invalid_inputs.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

src = 'invalid_source', dst = 'destination_dir', overwrite = False

    def copy_tree(src: PathType, dst: PathType, overwrite: bool = False) -> None:
        r"""Copy contents of folder ``src`` to folder ``dst``. The ``dst`` folder can exist or whatever (looking at you,
        :py:func:`shutil.copytree`).
    
        :param src: The source directory.
        :param dst: The destination directory. If it doesn't exist, it will be created.
        :param overwrite: If ``True``, files in ``dst`` will be overwritten if a file with the same relative path exists
            in ``src``. If ``False``, these files are not copied. Defaults to ``False``.
        """
        os.makedirs(dst, exist_ok=True)
>       for file in os.listdir(src):
E       FileNotFoundError: [Errno 2] No such file or directory: 'invalid_source'

flutes/flutes/fs.py:119: FileNotFoundError

During handling of the above exception, another exception occurred:

    def test_invalid_inputs():
        # Test invalid source path
        try:
            copy_tree("invalid_source", "destination_dir")
        except FileNotFoundError as e:
>           assert str(e) == "No such file or directory: 'invalid_source'"
E           assert "[Errno 2] No...valid_source'" == "No such file...valid_source'"
E             
E             - No such file or directory: 'invalid_source'
E             + [Errno 2] No such file or directory: 'invalid_source'
E             ? ++++++++++

flutes/Test4DT_tests/test_flutes_fs_copy_tree_1_test_invalid_inputs.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_copy_tree_1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.11s ===============================
"""