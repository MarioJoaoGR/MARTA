
import pytest
from tornado.locks import Lock, Semaphore

class _ReleasingContextManager:
    """A context manager that releases a Lock or Semaphore at the end of a "with" statement."""
    
    def __init__(self, obj):
        self._obj = obj

    def __enter__(self):
        return self._obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if isinstance(self._obj, Lock) or isinstance(self._obj, Semaphore):
            if exc_type is None:  # No exception occurred
                self._obj.release()
            else:  # An exception occurred
                pass  # Do nothing on exception to ensure release happens only when no exceptions occur
        else:
            raise TypeError("The provided object must be a Lock or Semaphore instance.")

# Test for valid lock usage

# Test for invalid semaphore input (should raise TypeError)
def test_invalid_semaphore_input():
    with pytest.raises(TypeError):
        with _ReleasingContextManager("not a Lock or Semaphore"):
            pass

# Test for valid semaphore usage