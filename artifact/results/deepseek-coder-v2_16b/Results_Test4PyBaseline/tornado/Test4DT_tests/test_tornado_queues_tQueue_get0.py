# Module: tornado.queues
# Import the function using its provided module name.
from tornado.queues import Queue
import pytest
import asyncio

@pytest.fixture
def queue():
    return Queue(maxsize=2)

@pytest.mark.asyncio
async def test_put_and_get(queue):
    # Put items into the queue
    await queue.put(0)
    assert len(queue._queue) == 1
    await queue.put(1)
    assert len(queue._queue) == 2
    
    # Get items from the queue
    item = await queue.get()
    assert item == 0
    assert len(queue._queue) == 1
    item = await queue.get()
    assert item == 1
    assert len(queue._queue) == 0

@pytest.mark.asyncio
async def test_task_done(queue):
    # Put items into the queue
    await queue.put(0)
    await queue.put(1)
    
    # Get and task done for each item
    item = await queue.get()
    assert item == 0
    queue.task_done()
    assert queue._unfinished_tasks == 1
    
    item = await queue.get()
    assert item == 1
    queue.task_done()
    assert queue._unfinished_tasks == 0

@pytest.mark.asyncio
async def test_join(queue):
    # Start a consumer coroutine
    async def consumer():
        while True:
            await queue.get()
            queue.task_done()
    
    # Spawn the consumer without waiting
    queue.spawn_callback(consumer)
    
    # Put items into the queue
    for i in range(5):
        await queue.put(i)
    
    # Wait for all tasks to be done
    await queue.join()
    assert queue._unfinished_tasks == 0

@pytest.mark.asyncio
async def test_get_with_timeout(queue):
    with pytest.raises(asyncio.TimeoutError):
        await queue.get(timeout=0.1)
