
import pytest
from tornado.queues import Queue

def test_valid_inputs():
    q = Queue(maxsize=2)
    assert q._maxsize == 2
    for item in range(2):
        q.put(item)
        assert q.qsize() == item + 1
    with pytest.raises(ValueError):
        Queue(maxsize=-1)
