
import pytest
from tornado.queues import Queue

def test_valid_inputs():
    q = Queue(maxsize=2)
    assert q._maxsize == 2
    assert len(q._putters) == 0
    assert len(q._getters) == 0

    # Adding items to the queue
    for item in range(2):
        q.put(item)
        assert q._unfinished_tasks == item + 1

def test_invalid_inputs():
    with pytest.raises(ValueError):
        Queue(maxsize=-1)
