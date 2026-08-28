
import pytest
from tornado.locks import Semaphore

# Test scenarios
def test_valid_case():
    # Setup: Real instance of Semaphore with minimal args
    sem = Semaphore(2)
    
    # Test that the semaphore can be acquired and released correctly
    assert sem._value == 2
    sem.acquire()
    assert sem._value == 1
    sem.release()
    assert sem._value == 2

def test_edge_case():
    # Setup: None (should raise TypeError since Semaphore requires an int value)
    with pytest.raises(TypeError):
        Semaphore(None)

def test_invalid_input():
    # Setup: None (should raise ValueError since the initial value must be >= 0)
    with pytest.raises(ValueError):
        Semaphore(-1)
