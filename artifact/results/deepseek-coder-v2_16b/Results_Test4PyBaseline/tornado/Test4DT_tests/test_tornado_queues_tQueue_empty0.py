
# Module: tornado.queues
# Import the Queue class from the tornado.queues module
from tornado.queues import Queue
import pytest

@pytest.fixture
def queue():
    return Queue(maxsize=2)

def test_queue_creation(queue):
    assert isinstance(queue, Queue)
    assert queue._maxsize == 2

def test_put_item(queue):
    queue.put(1)