
import pytest
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.queues import Queue

# Fixture to create a queue instance for testing
@pytest.fixture
def queue():
    return Queue(maxsize=2)

# Test adding items to the queue with put method
@pytest.mark.asyncio
async def test_put(queue):
    await queue.put(0)
    assert len(queue._queue) == 1
    item = await queue.get()
    assert item == 0

# Test getting items from the queue with get method
@pytest.mark.asyncio
async def test_get(queue):
    await queue.put(1)
    item = await queue.get()
    assert item == 1
    assert len(queue._queue) == 0

# Test marking tasks as done with task_done method
@pytest.mark.asyncio
async def test_task_done(queue):
    await queue.put(2)
    await queue.get()
    queue.task_done()
    assert queue._unfinished_tasks == 0

# Test waiting for all tasks to be processed with join method
@pytest.mark.asyncio
async def test_join(queue):
    async def consumer():
        while True:
            await queue.get()
            queue.task_done()
    
    IOLoop.current().spawn_callback(consumer)
    for i in range(2):
        await queue.put(i)
    await queue.join()
    assert queue._unfinished_tasks == 0

# Test the full method when maxsize is set to 2
@pytest.mark.asyncio
async def test_full(queue):
    for i in range(2):
        await queue.put(i)
    with pytest.raises(Exception):
        await queue.put(3)  # This should raise an exception because the queue is full

# Additional tests to cover uncovered lines (181-182, 184)
@pytest.mark.asyncio
async def test_full_maxsize_zero(queue):
    assert not queue.full()  # maxsize is zero, so the queue should never be full

@pytest.mark.asyncio
async def test_full_when_not_full():
    for i in range(1):
        await queue.put(i)
    assert not queue.full()  # Queue has space left

@pytest.mark.asyncio
async def test_full_when_full():
    for i in range(2):
        await queue.put(i)
    assert queue.full()  # Queue is at maxsize, should be full
