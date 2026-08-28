# Module: tornado.queues
import pytest
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.queues import Queue

# Fixture to create a queue instance for testing
@pytest.fixture
def queue():
    return Queue(maxsize=2)

# Test adding items to the queue by producer
@pytest.mark.asyncio
async def test_queue_put(queue):
    async def producer():
        for item in range(5):
            await queue.put(item)
            assert len(queue._queue) == item + 1, f"Queue size should be {item + 1} after putting item {item}"
            print('Put %s' % item)
    
    await producer()

# Test consuming items from the queue by consumer
@pytest.mark.asyncio
async def test_queue_get(queue):
    async def consumer():
        for i in range(5):
            item = await queue.get()
            assert item == i, f"Item should be {i} but got {item}"
            print('Doing work on %s' % item)
            queue.task_done()
    
    IOLoop.current().spawn_callback(consumer)
    await gen.sleep(0.1)  # Wait for consumer to process items

# Test waiting for all tasks to be processed
@pytest.mark.asyncio
async def test_queue_join(queue):
    async def producer():
        for item in range(5):
            await queue.put(item)
            print('Put %s' % item)
    
    async def consumer():
        for _ in range(5):
            await queue.get()
            queue.task_done()
    
    IOLoop.current().spawn_callback(consumer)
    await producer()  # Wait for producer to put all tasks
    await queue.join()  # Wait for consumer to finish all tasks
    assert queue._unfinished_tasks == 0, "All tasks should be processed"
    print('Done')

# Test using the queue in an asynchronous for loop
@pytest.mark.asyncio
async def test_queue_aiter(queue):
    async def producer():
        for item in range(5):
            await queue.put(item)
            print('Put %s' % item)
    
    async def consume_items():
        async for item in queue:
            assert isinstance(item, int), "Items should be integers"
            print('Processing item:', item)  # Process the item (replace with actual processing logic)
    
    IOLoop.current().spawn_callback(producer)
    await consume_items()
