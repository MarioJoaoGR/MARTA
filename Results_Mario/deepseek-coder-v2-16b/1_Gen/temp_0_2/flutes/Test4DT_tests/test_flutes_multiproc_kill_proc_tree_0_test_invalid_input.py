
import pytest
import os
from psutil import NoSuchProcess, ZombieProcess

def kill_proc_tree(pid: int, including_parent: bool = True) -> None:
    """Kill all child processes of a given process.

    This function kills the specified process and all its descendant processes. It uses the `psutil` library to manage system processes.

    Parameters:
        pid (int): The process ID (PID) of the parent process whose children you want to kill. To commit suicide, use `os.getpid`.
        including_parent (bool): If ``True``, the parent process itself will be killed along with its children. Defaults to ``True``.
    """
    import psutil
    parent = psutil.Process(pid)
    children = parent.children(recursive=True)
    for child in children:
        child.kill()
    _ = psutil.wait_procs(children, timeout=5)
    if including_parent:
        parent.kill()
        parent.wait(5)

def test_invalid_input():
    with pytest.raises(TypeError):
        kill_proc_tree("invalid_pid")  # Providing a non-integer value for PID
        kill_proc_tree(1234.56)         # Providing a float instead of an integer for PID
