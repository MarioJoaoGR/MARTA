
import pytest
import os
import psutil
from flutes.multiproc import kill_proc_tree

@pytest.mark.skip(reason="This test is disabled because it requires mocking psutil for the edge case scenario.")
def test_kill_proc_tree():
    # Test killing a process and its children
    with pytest.raises(psutil.NoSuchProcess):
        kill_proc_tree(os.getpid(), including_parent=True)
    
    # Add assertions to verify the expected behavior
    parent_process = psutil.Process(os.getpid())
    assert not parent_process.is_running()  # Parent process should be terminated
