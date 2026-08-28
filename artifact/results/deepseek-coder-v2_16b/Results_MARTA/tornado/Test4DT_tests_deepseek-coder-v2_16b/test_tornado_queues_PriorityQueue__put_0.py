
import pytest
from tornado.queues import PriorityQueue



def test_valid_input():
    q = PriorityQueue()
    item = (1, 'item')
    q._put(item)
    assert len(q._queue) == 1
    assert q._queue[0] == item