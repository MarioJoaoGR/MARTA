
import pytest
from queue import Queue
from threading import Thread
from pytutils.queues import merge

# Helper function to push elements from one queue to another for testing purposes
def push(src, dest):
    while True:
        try:
            item = src.get_nowait()
            dest.put_nowait(item)
        except:
            break

@pytest.fixture
def setup_queues():
    q1 = Queue()
    q2 = Queue()
    q3 = Queue()
    return q1, q2, q3

def test_merge_with_three_queues(setup_queues):
    q1, q2, q3 = setup_queues
    out_q = merge(q1, q2, q3)
    
    # Add elements to the queues for testing
    q1.put(1)
    q2.put(2)
    q3.put(3)
    
    assert out_q.get() == 1
    assert out_q.get() == 2