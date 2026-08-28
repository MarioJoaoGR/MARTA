# Module: tornado.queues
import pytest
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.queues import Queue

# Fixture to create a queue instance for testing
@pytest.fixture(scope="module")
def queue():
    return Queue(maxsize=2)

# Test adding an item to the queue by the producer
@pytest.mark.asyncio
async def test_put(queue):
    await queue.put(0)
    assert len(queue._queue) == 1
    assert list(queue._queue) == [0]

# Test getting an item from the queue by the consumer
@pytest.mark.asyncio
async def test_get(queue):
    # Add items to the queue first
    await queue.put(1)
    await queue.put(2)
    
    # Get an item from the queue
    item = await queue.get()
    assert item == 1
    assert len(queue._queue) == 1
    assert list(queue._queue) == [2]

# Test marking a task as done by the consumer
@pytest.mark.asyncio
async def test_task_done(queue):
    # Add items to the queue first
    await queue.put(3)
    await queue.put(4)
    
    # Get an item from the queue and mark it as done
    await queue.get()
    queue.task_done()
    assert queue._unfinished_tasks == 1
    
    # Get another item from the queue and mark it as done
    await queue.get()
    queue.task_done()
    assert queue._unfinished_tasks == 0

# Test waiting for all tasks to be processed by joining the queue
@pytest.mark.asyncio
async def test_join(queue):
    # Add items to the queue first
    await queue.put(5)
    await queue.put(6)
    
    # Start a consumer coroutine
    async def consumer():
        while True:
            item = await queue.get()
            try:
                print('Doing work on %s' % item)  # Simulate some work with a sleep
                await gen.sleep(0.01)
            finally:
                queue.task_done()
    
    IOLoop.current().spawn_callback(consumer)
    
    # Wait for the producer to put all tasks
    async def producer():
        for item in range(7, 9):
            await queue.put(item)
            print('Put %s' % item)
    
    await producer()
    
    # Wait for consumer to finish all tasks by joining the queue
    await queue.join()
    assert queue._unfinished_tasks == 0
    print('Done')
