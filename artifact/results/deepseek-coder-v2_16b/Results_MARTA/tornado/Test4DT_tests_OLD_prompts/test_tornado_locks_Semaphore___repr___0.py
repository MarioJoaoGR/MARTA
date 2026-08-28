
import pytest
from tornado.locks import Semaphore

def test_semaphore_initialization():
    with pytest.raises(ValueError):
        Semaphore(-1)  # Test with an invalid initial value (negative number)
    sem = Semaphore(0)  # Test with the boundary value of zero
    assert sem._value == 0

def test_acquire_release():
    sem = Semaphore(2)
    for _ in range(2):
        sem.acquire()
    assert sem._value == 0
    sem.release()
    sem.release()
    assert sem._value == 2

def test_context_manager():
    sem = Semaphore(1)
    with pytest.raises(RuntimeError):  # Attempt to acquire when semaphore is locked
        with sem:
            pass
