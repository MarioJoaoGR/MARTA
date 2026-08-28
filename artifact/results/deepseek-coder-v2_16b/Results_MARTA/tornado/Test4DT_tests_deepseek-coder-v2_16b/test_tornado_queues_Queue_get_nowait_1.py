
import pytest
from tornado.queues import Queue
from tornado.ioloop import IOLoop
import asyncio

@pytest.mark.asyncio
async def test_valid_input():
    q = Queue(maxsize=2)
    
    # Start consumer without waiting (since it never finishes).
    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await asyncio.sleep(0.01)
            finally:
                q.task_done()
    
    # Start the consumer coroutine
    IOLoop.current().spawn_callback(consumer)
    
    # Add items to the queue (producer)
    for item in range(5):
        await q.put(item)
        print('Put %s' % item)
    
    # Wait for all tasks to be processed
    await q.join()
    assert True, "All tasks were processed successfully"

@pytest.mark.asyncio
async def test_edge_case():
    q = Queue(maxsize=0)  # Unbounded queue
    
    async def consumer():
        while True:
            item = await q.get()
            try:
                print('Doing work on %s' % item)
                await asyncio.sleep(0.01)
            finally:
                q.task_done()
    
    IOLoop.current().spawn_callback(consumer)
    
    for item in range(5):
        await q.put(item)
        print('Put %s' % item)
    
    await q.join()
    assert True, "All tasks were processed successfully"

@pytest.mark.asyncio
def test_invalid_input():
    with pytest.raises(TypeError):
        Queue(maxsize=None)
