
# Module: tornado.queues
import pytest
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.queues import Queue

# Fixture to create a queue instance for testing
@pytest.fixture
def queue():
    return Queue(maxsize=2)

# Test the full method when maxsize is set to 2
@pytest.mark.asyncio
async def test_full(queue):
    # Fill the queue to its maximum size
    for i in range(2):
        await queue.put(i)
    
    # Check that the queue is full
    assert queue.full() == True

# Test the full method when maxsize is set to 0 (no limit)
@pytest.fixture
def unlimited_queue():
    return Queue()

@pytest.mark.asyncio
async def test_full_unlimited(unlimited_queue):
    # Add items without reaching the maximum size
    await unlimited_queue.put(0)
    await unlimited_queue.put(1)
    
    # Check that the queue is not full since there's no limit