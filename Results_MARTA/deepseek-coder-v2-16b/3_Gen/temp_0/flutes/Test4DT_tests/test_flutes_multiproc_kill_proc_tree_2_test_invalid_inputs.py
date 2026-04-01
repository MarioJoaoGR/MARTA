
import pytest
from unittest.mock import patch, MagicMock
import psutil

def kill_proc_tree(pid: int, including_parent: bool = True) -> None:
    """Kill all child processes of a given process.

    This function is designed to terminate all child processes associated with the specified PID (process ID). It leverages the `psutil` library to interact with the operating system's process table, enabling both graceful termination and immediate killing based on the provided flag.

    Parameters:
        pid (int): The process ID (PID) of the parent process whose children should be terminated. To terminate the current process, use `os.getpid`.
        including_parent (bool): If ``True``, the function will also attempt to kill the parent process itself. Defaults to ``True``.
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

def test_invalid_inputs():
    with patch('psutil.Process', side_effect=Exception("Mocked exception")):
        with pytest.raises(Exception):
            kill_proc_tree(1234)
