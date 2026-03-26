
import pytest
from flutes.multiproc import kill_proc_tree
import psutil
import os

@pytest.mark.skipif(not psutil.pid_exists(os.getpid()), reason="Test requires a running process")
def test_valid_case():
    # Start a new process for testing (this is just an example, the actual process should be started differently)
    import subprocess
    proc = subprocess.Popen(['sleep', '10'])  # This will run sleep command in a new process
    
    try:
        assert psutil.pid_exists(proc.pid), "Initial process not found"
        
        kill_proc_tree(proc.pid, including_parent=True)
        
        # Wait for the process to terminate
        proc.wait(timeout=5)
        assert not psutil.pid_exists(proc.pid), "Process did not terminate after calling kill_proc_tree"
    finally:
        # Ensure the subprocess is properly terminated even if the test fails
        proc.terminate()
