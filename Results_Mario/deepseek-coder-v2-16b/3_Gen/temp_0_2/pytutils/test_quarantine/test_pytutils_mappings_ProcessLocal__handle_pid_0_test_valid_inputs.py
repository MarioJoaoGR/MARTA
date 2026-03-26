
import os
from collections import MutableMapping

class ProcessLocal(dict):
    """
    Provides a basic per-process mapping container that wipes itself if the current PID changed since the last get/set. Aka `threading.local()`, but for processes instead of threads.

    Parameters:
        mapping_factory (callable, optional): A factory function or class used to create a new dictionary when the process ID changes. This should be a callable that returns an instance of a mutable mapping type like dict. Defaults to `dict`.

    Examples:
        Creating and using a ProcessLocal instance:
            >>> plocal = ProcessLocal()
            >>> plocal['test'] = True
            >>> print(plocal['test'])  # Output: True
        
        Emulating a PID change by forcing it to be something invalid:
            >>> plocal._handle_pid(new_pid=-1)
            >>> print(plocal['test'])  # Raises KeyError since the mapping has been wiped.

    Note:
        - Changes to `mapping_factory` will affect how new dictionaries are created when the PID changes, ensuring that data remains isolated between processes.
        - Calling `_handle_pid()` manually with a different PID can be used to simulate a change in the process ID and observe how the internal mapping is updated accordingly.
    """
    __pid__ = -1
    
    def __init__(self, mapping_factory=dict):
        self.__mapping_factory = mapping_factory
        self._handle_pid()

    def _handle_pid(self, new_pid=os.getpid):
        if callable(new_pid):
            new_pid = new_pid()

        if self.__pid__ != new_pid:
            self.__pid__, self.__mapping = new_pid, self.__mapping_factory()
            super().__init__(self.__mapping)  # Initialize the dictionary with the new mapping

    def __getitem__(self, key):
        return self.__mapping[key]

    def __setitem__(self, key, value):
        self.__mapping[key] = value

# Now let's write a test case to ensure that the ProcessLocal class behaves as expected.
import pytest

@pytest.fixture
def plocal():
    return ProcessLocal()

def test_valid_inputs(plocal):
    plocal['test'] = True
    assert plocal['test'] == True
    old_pid = os.getpid()
    plocal._handle_pid(new_pid=lambda: -1)  # Force a PID change by returning an invalid value
    with pytest.raises(KeyError):
        print(plocal['test'])  # This should raise KeyError because the mapping has been wiped

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_mappings_ProcessLocal__handle_pid_0_test_valid_inputs
pytutils/Test4DT_tests/test_pytutils_mappings_ProcessLocal__handle_pid_0_test_valid_inputs.py:3:0: E0611: No name 'MutableMapping' in module 'collections' (no-name-in-module)


"""