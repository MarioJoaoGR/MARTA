
import pytest
from tornado.locks import Semaphore

# Test scenarios
def test_valid_input():
    sem = Semaphore(2)  # Setup: valid initial value
    assert sem._value == 2
    sem.acquire()
    sem.acquire()
    sem.release()
    assert sem._value == 1

def test_edge_case():
    try:
        sem = Semaphore(-1)  # Setup: negative initial value, should raise ValueError
    except ValueError as e:
        pass
    else:
        pytest.fail("Expected ValueError for negative initial value")

def test_invalid_input():
    sem = Semaphore(2)  # Setup: valid initial value
    with pytest.raises(TypeError):
        sem.release(None)  # Release with invalid input, should raise TypeError or ValueError
