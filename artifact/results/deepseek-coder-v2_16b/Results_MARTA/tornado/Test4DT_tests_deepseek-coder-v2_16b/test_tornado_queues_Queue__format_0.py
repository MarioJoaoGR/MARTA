
import pytest
from tornado.queues import Queue

def test_valid_input():
    q = Queue(maxsize=2)
    assert q.maxsize == 2

    # Put some items into the queue
    for item in range(2):
        q.put(item)
        assert len(q._queue) == item + 1

def test_invalid_input():
    with pytest.raises(ValueError):
        Queue(maxsize=-1)
