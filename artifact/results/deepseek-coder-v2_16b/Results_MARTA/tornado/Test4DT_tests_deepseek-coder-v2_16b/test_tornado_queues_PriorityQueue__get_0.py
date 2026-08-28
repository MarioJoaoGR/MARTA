
import pytest
from tornado.queues import PriorityQueue

def test_priority_queue_ordering():
    q = PriorityQueue()
    q.put((1, 'medium-priority item'))
    q.put((0, 'high-priority item'))
    q.put((10, 'low-priority item'))
    
    assert q.get_nowait() == (0, 'high-priority item')
    assert q.get_nowait() == (1, 'medium-priority item')
    assert q.get_nowait() == (10, 'low-priority item')

def test_priority_queue_empty():
    q = PriorityQueue()
    
    with pytest.raises(Exception):
        q.get_nowait()
