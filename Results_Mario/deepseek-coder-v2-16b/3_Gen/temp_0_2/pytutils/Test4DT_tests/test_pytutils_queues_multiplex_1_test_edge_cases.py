
import pytest
from queue import Queue
from pytutils.queues import multiplex

def test_edge_cases():
    in_q = Queue()
    
    # Test with None count
    with pytest.raises(TypeError):
        q1, q2 = multiplex(in_q, count=None)
