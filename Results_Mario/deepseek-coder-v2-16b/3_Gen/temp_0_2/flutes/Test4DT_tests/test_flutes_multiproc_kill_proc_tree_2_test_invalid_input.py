
import pytest
from flutes.multiproc import kill_proc_tree
import psutil

def test_invalid_input():
    with pytest.raises(TypeError):
        kill_proc_tree("invalid_pid", including_parent=True)
