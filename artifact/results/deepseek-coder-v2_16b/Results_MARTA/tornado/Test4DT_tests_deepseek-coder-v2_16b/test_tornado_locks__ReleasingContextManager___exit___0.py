
import pytest
from tornado.locks import Lock, BoundedSemaphore

class _ReleasingContextManager:
    """A context manager that releases a Lock or Semaphore at the end of a "with" statement."""
    
    def __init__(self, obj):
        self._obj = obj

    def __enter__(self):
        if isinstance(self._obj, (Lock, BoundedSemaphore)):
            return self._obj
        else:
            raise TypeError("The object must be a Lock or Semaphore instance.")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._obj.release()

def test_valid_case():
    lock = Lock()
    cm = _ReleasingContextManager(lock)
    with pytest.raises(RuntimeError):  # Ensure the context manager raises RuntimeError if not used correctly
        with cm:
            pass

def test_error_case():
    from tornado.locks import BoundedSemaphore
    sem = BoundedSemaphore(value=2)
    for _ in range(3):
        try:
            sem.release()
        except ValueError as e:
            assert str(e) == "Semaphore released too many times"  # Adjust this assertion based on actual error message
