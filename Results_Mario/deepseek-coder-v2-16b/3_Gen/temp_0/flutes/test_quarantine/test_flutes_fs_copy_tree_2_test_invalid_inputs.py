
import pytest
from flutes.fs import copy_tree
import os
import shutil

def test_invalid_inputs():
    with pytest.raises(FileNotFoundError):
        copy_tree('/nonexistent/source', '/nonexistent/destination')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_fs_copy_tree_2_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.raises(FileNotFoundError):
>           copy_tree('/nonexistent/source', '/nonexistent/destination')

flutes/Test4DT_tests/test_flutes_fs_copy_tree_2_test_invalid_inputs.py:9: 
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
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_copy_tree_2_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.12s ===============================
"""