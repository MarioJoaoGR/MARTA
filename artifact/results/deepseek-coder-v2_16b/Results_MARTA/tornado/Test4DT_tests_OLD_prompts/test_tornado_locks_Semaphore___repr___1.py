
import pytest
from tornado.locks import Semaphore

def test_valid_inputs():
    sem = Semaphore(2)
    assert sem._value == 2

def test_edge_cases():
    with pytest.raises(ValueError):
        Semaphore(-1)  # Initial value less than 0 should raise a ValueError
    
    sem = Semaphore(0)
    assert sem._value == 0

def test_invalid_inputs():
    with pytest.raises(ValueError):
        Semaphore(-1)  # Initial value less than 0 should raise a ValueError
    
    sem = Semaphore(2)
    assert sem._value == 2
