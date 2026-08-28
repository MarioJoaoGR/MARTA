
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
    assert not queue.empty()

# New test case to check the empty method when the queue is not empty
def test_not_empty_after_put(queue):
    queue.put(1)
    assert not queue.empty()

# New test case to check the empty method when the queue is initially empty
def test_empty_when_initially_empty(queue):
    assert queue.empty()
