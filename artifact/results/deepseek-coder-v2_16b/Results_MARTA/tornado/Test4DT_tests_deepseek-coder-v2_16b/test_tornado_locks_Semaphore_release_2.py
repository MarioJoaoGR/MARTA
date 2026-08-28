
import pytest
from tornado.locks import Semaphore

# Test scenario 1: test_valid_input - Test standard input for Semaphore.release with valid initial value
def test_valid_input():
    sem = Semaphore(2)
    assert sem._value == 2
    sem.release()
    assert sem._value == 3
    sem.release()
    assert sem._value == 4

# Test scenario 2: test_edge_case - Test edge case where no additional setup is needed
def test_edge_case():
    sem = Semaphore(1)
    assert sem._value == 1
    sem.release()
    assert sem._value == 2
    sem.release()
    assert sem._value == 3

# Test scenario 3: test_invalid_input - Test raising ValueError for Semaphore.release with invalid initial value
def test_invalid_input():
    try:
        sem = Semaphore(-1)
    except ValueError as e:
        assert str(e) == 'semaphore initial value must be >= 0'
