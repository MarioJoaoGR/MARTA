
import pytest
from queue import Queue
from threading import Thread
from pytutils.queues import merge

# Helper function to simulate pushing elements from one queue to another
def push(in_q, out_q):
    while True:
        item = in_q.get()
        if item is None:  # Sentinel value to indicate end of queue
            break
        out_q.put(item)

# Test cases for the merge function
def test_merge_with_three_queues():
    q1, q2, q3 = [Queue() for _ in range(3)]
    out_q = merge(q1, q2, q3)
    
    # Add elements to each input queue
    q1.put('a')
    q2.put('b')
    q3.put('c')
    
    # Check if the output queue contains the merged elements
    assert out_q.get() == 'a'  # First element from q1