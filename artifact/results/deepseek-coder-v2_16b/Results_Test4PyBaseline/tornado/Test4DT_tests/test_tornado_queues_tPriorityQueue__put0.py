
import pytest
from tornado.queues import PriorityQueue
import heapq

@pytest.fixture
def priority_queue():
    return PriorityQueue()

def test_priority_queue_put(priority_queue):
    # Add items to the queue with different priorities
    priority_queue._put((1, 'medium-priority item'))  # Adding an item with medium priority
    priority_queue._put((0, 'high-priority item'))    # Adding an item with high priority
    priority_queue._put((10, 'low-priority item'))    # Adding an item with low priority

    # Retrieve and check the items in order of priority
    assert priority_queue.get_nowait() == (0, 'high-priority item')
    assert priority_queue.get_nowait() == (1, 'medium-priority item')
    assert priority_queue.get_nowait() == (10, 'low-priority item')

def test_priority_queue_put_specific_priorities(priority_queue):
    # Add items to the queue with specific priorities
    priority_queue._put((5, 'item with high priority'))  # Adding an item with a specific high priority
    priority_queue._put((3, 'item with medium priority')) # Adding an item with a specific medium priority
    priority_queue._put((1, 'item with low priority'))    # Adding an item with a specific low priority

    # Retrieve and check the items in order of priority
    assert priority_queue.get_nowait() == (1, 'item with low priority')
    assert priority_queue.get_nowait() == (3, 'item with medium priority')
    assert priority_queue.get_nowait() == (5, 'item with high priority')

def test_priority_queue_put_multiple():
    # Create a priority queue instance
    q = PriorityQueue()

    # Add multiple items to the queue with different priorities
    q._put((1, 'medium-priority item'))
    q._put((0, 'high-priority item'))
    q._put((10, 'low-priority item'))
    q._put((2, 'slightly higher priority item'))
    q._put((1, 'same as first medium priority'))

    # Retrieve and check the items in order of priority
    assert q.get_nowait() == (0, 'high-priority item')
    assert q.get_nowait() == (1, 'medium-priority item')