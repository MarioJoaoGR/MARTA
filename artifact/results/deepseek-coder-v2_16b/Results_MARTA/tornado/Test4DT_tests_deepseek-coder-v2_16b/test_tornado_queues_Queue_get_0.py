
import pytest
from tornado.queues import Queue
from tornado.ioloop import IOLoop
import asyncio

# Test for checking if the queue is initialized correctly with maxsize=2
def test_queue_initialization():
    q = Queue(maxsize=2)
    assert q._maxsize == 2

# Test for adding items to the queue and verifying its size
@pytest.mark.asyncio
async def test_put_items():
    q = Queue(maxsize=2)
    for item in range(2):
        q.put(item)
    assert len(q._queue) == 2

# Test for getting items from the queue and verifying its size after retrieval
@pytest.mark.asyncio
async def test_get_items():
    q = Queue(maxsize=2)
    for item in range(2):
        q.put(item)
    item1 = await q.get()
    item2 = await q.get()
    assert len(q._queue) == 0
    assert item1 is not None and item2 is not None

# Test for checking if the queue raises QueueFull when maxsize is reached
@pytest.mark.asyncio
async def test_queue_full():
    q = Queue(maxsize=2)
    with pytest.raises(QueueFull):
        q.put(1)
        q.put(2)
        q.put(3)  # This should raise QueueFull error

# Test for checking if the queue raises TimeoutError when getting with timeout
@pytest.mark.asyncio
async def test_get_with_timeout():
    q = Queue(maxsize=2)
    with pytest.raises(TimeoutError):
        await q.get(timeout=0.1)  # This should raise TimeoutError after 0.1 seconds
