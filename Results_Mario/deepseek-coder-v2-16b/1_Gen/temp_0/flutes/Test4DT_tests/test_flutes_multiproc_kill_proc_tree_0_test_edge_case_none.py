
import pytest
from flutes.multiproc import kill_proc_tree
import os
import psutil
import sys
import time

@pytest.mark.skipif(sys.platform != 'linux', reason="This test is for Linux only")
def test_edge_case_none():
    # Create a mock child process to simulate the parent process
    pid = os.getpid()
    kill_proc_tree(pid, including_parent=False)
    
    # Check if the current process (parent) is still running
    parent = psutil.Process(pid)
    assert parent.is_running(), "The parent process should not be terminated"
