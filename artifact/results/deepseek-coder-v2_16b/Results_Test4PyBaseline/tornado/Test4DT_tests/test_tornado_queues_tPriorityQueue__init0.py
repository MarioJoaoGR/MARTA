
import pytest
from tornado.queues import PriorityQueue

def test_priority_queue():
    q = PriorityQueue()
    
    # Add items with different priorities
    q.put((1, 'medium-priority item'))
    q.put((0, 'high-priority item'))
    q.put((10, 'low-priority item'))
    
    # Retrieve items in ascending order of priority
    assert q.get_nowait() == (0, 'high-priority item')
    assert q.get_nowait() == (1, 'medium-priority item')
    assert q.get_nowait() == (10, 'low-priority item')

def test_empty_queue():
    q = PriorityQueue()
    
    # Attempt to get an item from an empty queue
    with pytest.raises(Exception):
        q.get_nowait()

def test_multiple_items_same_priority():
    q = PriorityQueue()
    
    # Add multiple items with the same priority
    q.put((1, 'item 1'))
    q.put((1, 'item 2'))
    q.put((1, 'item 3'))
    
    # Retrieve items in arbitrary order since they have the same priority
    retrieved_items = [q.get_nowait() for _ in range(3)]
    assert (1, 'item 1') in retrieved_items
    assert (1, 'item 2') in retrieved_items
    assert (1, 'item 3') in retrieved_items
