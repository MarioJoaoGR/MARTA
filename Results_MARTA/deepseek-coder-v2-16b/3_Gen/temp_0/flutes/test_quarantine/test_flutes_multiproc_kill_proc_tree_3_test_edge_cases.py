
import pytest
from flutes.multiproc import kill_proc_tree
import psutil
import os

@pytest.fixture(autouse=True)
def mock_psutil():
    # Mocking psutil to simulate process interactions
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(psutil, 'Process', lambda x: FakeProcess(x))
        yield

class FakeProcess:
    def __init__(self, pid):
        self.pid = pid
    
    def children(self, recursive=True):
        # Return fake child processes for testing
        return [FakeProcess(i) for i in range(10)]
    
    def kill(self):
        pass  # Simulate killing the process
    
    def wait(self, timeout=5):
        pass  # Simulate waiting for the process to terminate

def test_kill_proc_tree():
    pid = os.getpid()
    kill_proc_tree(pid)
    assert not psutil.Process(pid).is_running(), "Parent process should be terminated"
    for child in psutil.Process(pid).children():
        assert not child.is_running(), "Child processes should be terminated"

def test_kill_proc_tree_including_parent():
    pid = os.getpid()
    kill_proc_tree(pid, including_parent=True)
    assert not psutil.Process(pid).is_running(), "Parent process should be terminated"
    for child in psutil.Process(pid).children():
        assert not child.is_running(), "Child processes should be terminated"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_multiproc_kill_proc_tree_3_test_edge_cases.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________________ test_kill_proc_tree ______________________________

    def test_kill_proc_tree():
        pid = os.getpid()
>       kill_proc_tree(pid)

flutes/Test4DT_tests/test_flutes_multiproc_kill_proc_tree_3_test_edge_cases.py:30: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/multiproc.py:790: in kill_proc_tree
    _ = psutil.wait_procs(children, timeout=5)
/usr/local/lib/python3.11/site-packages/psutil/__init__.py:1647: in wait_procs
    check_gone(proc, timeout)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

proc = <Test4DT_tests.test_flutes_multiproc_kill_proc_tree_3_test_edge_cases.FakeProcess object at 0x7f1553031210>
timeout = 0.1

    def check_gone(proc, timeout):
        try:
            returncode = proc.wait(timeout=timeout)
        except (TimeoutExpired, subprocess.TimeoutExpired):
            pass
        else:
>           if returncode is not None or not proc.is_running():
E           AttributeError: 'FakeProcess' object has no attribute 'is_running'

/usr/local/lib/python3.11/site-packages/psutil/__init__.py:1613: AttributeError
_____________________ test_kill_proc_tree_including_parent _____________________

    def test_kill_proc_tree_including_parent():
        pid = os.getpid()
>       kill_proc_tree(pid, including_parent=True)

flutes/Test4DT_tests/test_flutes_multiproc_kill_proc_tree_3_test_edge_cases.py:37: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/multiproc.py:790: in kill_proc_tree
    _ = psutil.wait_procs(children, timeout=5)
/usr/local/lib/python3.11/site-packages/psutil/__init__.py:1647: in wait_procs
    check_gone(proc, timeout)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

proc = <Test4DT_tests.test_flutes_multiproc_kill_proc_tree_3_test_edge_cases.FakeProcess object at 0x7f1552ebaa10>
timeout = 0.1

    def check_gone(proc, timeout):
        try:
            returncode = proc.wait(timeout=timeout)
        except (TimeoutExpired, subprocess.TimeoutExpired):
            pass
        else:
>           if returncode is not None or not proc.is_running():
E           AttributeError: 'FakeProcess' object has no attribute 'is_running'

/usr/local/lib/python3.11/site-packages/psutil/__init__.py:1613: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_kill_proc_tree_3_test_edge_cases.py::test_kill_proc_tree
FAILED flutes/Test4DT_tests/test_flutes_multiproc_kill_proc_tree_3_test_edge_cases.py::test_kill_proc_tree_including_parent
============================== 2 failed in 0.22s ===============================
"""