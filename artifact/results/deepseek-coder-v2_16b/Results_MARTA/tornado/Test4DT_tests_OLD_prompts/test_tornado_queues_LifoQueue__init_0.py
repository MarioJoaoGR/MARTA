
import pytest
from tornado.queues import LifoQueue

def test_valid_inputs():
    q = LifoQueue()
    q.put(3)
    q.put(2)
    q.put(1)
    
    assert q.get_nowait() == 1
    assert q.get_nowait() == 2
    assert q.get_nowait() == 3
