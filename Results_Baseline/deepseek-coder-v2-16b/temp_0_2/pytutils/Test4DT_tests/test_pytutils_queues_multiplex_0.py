
import pytest
from queue import Queue
from threading import Thread
from pytutils.queues import multiplex

def test_multiplex():
    in_q = Queue()
    q1, q2, q3 = multiplex(in_q, count=3)
    
    # Add items to the input queue
    in_q.put('item1')
    in_q.put('item2')
    in_q.put('item3')
    
    # Check if the output queues have received the items
    assert q1.get() == 'item1'