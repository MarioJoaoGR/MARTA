
import pytest
from flutes.multiproc import kill_proc_tree
import psutil
import os

def test_invalid_inputs():
    # Test with a non-integer PID
    with pytest.raises(TypeError):
        kill_proc_tree("invalid_pid", including_parent=True)
    
    # Test with a negative integer PID
    with pytest.raises(ValueError):
        kill_proc_tree(-1, including_parent=True)
