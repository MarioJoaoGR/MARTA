
import pytest
from queue import Queue

class NonQueue:
    pass

def push(in_q, out_q):
    while True:
        x = in_q.get()
        out_q.put(x)

def test_invalid_inputs():
    # Create non-queue objects
    in_q = NonQueue()
    out_q = NonQueue()
    
    # Attempt to call the push function with invalid inputs
    with pytest.raises(AttributeError):
        push(in_q, out_q)
