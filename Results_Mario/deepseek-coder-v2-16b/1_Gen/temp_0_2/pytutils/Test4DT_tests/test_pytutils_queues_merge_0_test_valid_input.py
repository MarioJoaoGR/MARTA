
import pytest
from queue import Queue
from threading import Thread
from pytutils.queues import merge

def test_valid_input():
    q1 = Queue()
    q2 = Queue()
    q3 = Queue()
    
    for i in range(5):
        q1.put(i)
        q2.put(i + 5)
        q3.put(i + 10)
    
    out_q = merge(q1, q2, q3)
    
    # Check if the output queue contains elements from all input queues
    for i in range(15):
        assert not out_q.empty()
        item = out_q.get()
        assert item == i
