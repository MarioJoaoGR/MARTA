
import pytest
from tornado.locks import Semaphore

def test_valid_case():
    sem = Semaphore(2)
    assert sem._value == 2

def test_edge_case():
    sem = Semaphore(0)
    assert sem._value == 0

def test_invalid_input():
    with pytest.raises(ValueError):
        sem = Semaphore(-1)
