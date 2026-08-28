
import pytest
from tornado.locks import Semaphore

def test_semaphore_initial_value():
    with pytest.raises(ValueError):
        Semaphore(-1)

def test_semaphore_default_value():
    sem = Semaphore()
    assert sem._value == 1
