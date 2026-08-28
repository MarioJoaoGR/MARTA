# Module: tornado.queues
import pytest
from tornado.queues import PriorityQueue
import heapq

@pytest.fixture
def setup_priority_queue():
    q = PriorityQueue()
    q.put((1, 'medium-priority item'))
    q.put((0, 'high-priority item'))
    q.put((10, 'low-priority item'))
    return q

def test_priority_queue_ordering(setup_priority_queue):
    queue = setup_priority_queue
    assert queue.get_nowait() == (0, 'high-priority item')
    assert queue.get_nowait() == (1, 'medium-priority item')
    assert queue.get_nowait() == (10, 'low-priority item')

def test_priority_queue_empty():
    q = PriorityQueue()
    with pytest.raises(Exception):
        q.get_nowait()  # Should raise an exception since the queue is empty
