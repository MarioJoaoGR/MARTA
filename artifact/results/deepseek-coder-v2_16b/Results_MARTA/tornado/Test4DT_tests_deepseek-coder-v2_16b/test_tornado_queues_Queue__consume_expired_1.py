
import pytest
from tornado.queues import Queue

def test_valid_input():
    q = Queue(maxsize=2)
    assert q._maxsize == 2

def test_edge_case_none():
    try:
        Queue(maxsize=None)
        pytest.fail("Expected TypeError")
    except TypeError:
        pass

def test_invalid_input():
    try:
        Queue(maxsize=-1)
        pytest.fail("Expected ValueError")
    except ValueError:
        pass
