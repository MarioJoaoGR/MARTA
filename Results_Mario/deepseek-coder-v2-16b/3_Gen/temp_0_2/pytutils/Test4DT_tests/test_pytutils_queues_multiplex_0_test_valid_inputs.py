
import pytest
from queue import Queue
from pytutils.queues import multiplex
from threading import Thread

def test_valid_inputs():
    in_q = Queue()
    q1, q2, q3 = multiplex(in_q, count=3)
    
    # Add items to the input queue
    in_q.put("item1")
    in_q.put("item2")
    
    # Check if the items are present in all output queues
    assert q1.get() == "item1"
    assert q2.get() == "item1"
    assert q3.get() == "item1"
    assert q1.get() == "item2"
    assert q2.get() == "item2"
    assert q3.get() == "item2"
    
    # Check if the queues are independent
    in_q.put("item3")
    assert q1.get() == "item3"
    assert q2.get() == "item3"
    assert q3.get() == "item3"
