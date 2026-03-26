
import pytest
from queue import Queue
from pytutils.queues import multiplex
from threading import Thread

def test_invalid_inputs():
    in_q = Queue()
    
    with pytest.raises(TypeError):
        q1, q2 = multiplex(in_q, count='a')
        
    with pytest.raises(ValueError):
        q3, q4 = multiplex(in_q, count=-5)
