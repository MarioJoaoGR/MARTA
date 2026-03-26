
import pytest
from flutes.multiproc import kill_proc_tree
import psutil
import os

def test_invalid_inputs():
    # Test case for invalid PID (non-integer)
    with pytest.raises(ValueError):
        kill_proc_tree("invalid_pid")
    
    # Test case for negative PID
    with pytest.raises(psutil.NoSuchProcess):
        kill_proc_tree(-1)
    
    # Test case for non-existing process (should raise psutil.NoSuchProcess)
    invalid_pid = os.getpid() + 9999  # Assuming this PID does not exist
    with pytest.raises(psutil.NoSuchProcess):
        kill_proc_tree(invalid_pid)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_kill_proc_tree_2_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test case for invalid PID (non-integer)
        with pytest.raises(ValueError):
>           kill_proc_tree("invalid_pid")

flutes/Test4DT_tests/test_flutes_multiproc_kill_proc_tree_2_test_invalid_inputs.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/multiproc.py:786: in kill_proc_tree
    parent = psutil.Process(pid)
/usr/local/lib/python3.11/site-packages/psutil/__init__.py:314: in __init__
    self._init(pid)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[AttributeError("'Process' object has no attribute '_pid'") raised in repr()] Process object at 0x7f49147a8990>
pid = 'invalid_pid', _ignore_nsp = False

    def _init(self, pid, _ignore_nsp=False):
        if pid is None:
            pid = os.getpid()
        else:
>           if pid < 0:
E           TypeError: '<' not supported between instances of 'str' and 'int'

/usr/local/lib/python3.11/site-packages/psutil/__init__.py:320: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_kill_proc_tree_2_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.14s ===============================

"""