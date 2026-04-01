
import os
import multiprocessing
import pytest
import psutil
from flutes.multiproc import kill_proc_tree

def test_valid_case():
    # Create a child process
    def target(queue):
        queue.put(os.getpid())
    
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=target, args=(q,))
    p.start()
    child_pid = q.get()
    p.join()
    
    # Kill the process tree including the parent
    kill_proc_tree(os.getpid(), including_parent=True)
    
    # Check if the parent and all children are killed
    assert not psutil.Process(os.getpid()).is_running()

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

flutes/Test4DT_tests/test_flutes_multiproc_kill_proc_tree_0_test_valid_case.py
"""