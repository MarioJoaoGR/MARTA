
import pytest
from tornado.queues import Queue, QueueFull, QueueEmpty

def test_error_put_nowait():
    q = Queue(maxsize=1)
    q.put_nowait(1)
    with pytest.raises(QueueFull):
        q.put_nowait(2)

def test_invalid_put_nowait():
    q = Queue()
    with pytest.raises(TypeError):
        q.put_nowait()
