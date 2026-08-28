
import pytest
from tornado.queues import Queue

# Test valid input scenario
def test_valid_input():
    q = Queue(maxsize=2)
    assert q._maxsize == 2
    assert len(q._getters) == 0
    assert len(q._putters) == 0

# Test edge case with None as maxsize scenario
def test_edge_case_none():
    with pytest.raises(TypeError):
        q = Queue(maxsize=None)

# Test raising ValueError with negative maxsize scenario
def test_invalid_input():
    with pytest.raises(ValueError):
        q = Queue(maxsize=-1)
