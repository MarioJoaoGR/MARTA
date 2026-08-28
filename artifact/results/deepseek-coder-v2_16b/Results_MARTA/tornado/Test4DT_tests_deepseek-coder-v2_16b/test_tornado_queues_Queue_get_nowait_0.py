
import pytest
from tornado.queues import Queue, QueueEmpty


def test_edge_case():
    q = Queue(maxsize=0)  # Unbounded queue
    with pytest.raises(TypeError):
        Queue(maxsize=None)
    
    q = Queue(maxsize=2)
    with pytest.raises(QueueEmpty):
        q.get_nowait()

def test_invalid_input():
    q = Queue(maxsize=2)
    with pytest.raises(QueueEmpty):
        q.get_nowait()