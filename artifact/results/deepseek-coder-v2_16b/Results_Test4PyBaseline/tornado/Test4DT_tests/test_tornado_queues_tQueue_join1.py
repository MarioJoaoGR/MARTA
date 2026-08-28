
# Module: tornado.queues
# test_queues.py
from tornado.queues import Queue
import pytest
import asyncio

@pytest.fixture
def queue():
    return Queue(maxsize=2)

@pytest.mark.asyncio
async def test_join_without_tasks(queue):
    with pytest.raises(asyncio.TimeoutError):
        await queue.join(timeout=0.1)

@pytest.mark.asyncio
async def test_join_with_tasks(queue):
    async def producer():
        for i in range(2):
            await queue.put(i)
    async def consumer():
        while True:
            item = await queue.get()
            print('Doing work on', item)
            await asyncio.sleep(0.01)  # Simulate some work with a sleep
            queue.task_done()
    import tornado.ioloop
    tornado.ioloop.IOLoop.current().spawn_callback(consumer)
    await producer()
    await queue.join()
    assert queue._unfinished_tasks == 0

@pytest.mark.asyncio
async def test_queue_with_maxsize():
    queue = Queue(maxsize=2)
    async def producer():
        for i in range(3):
            await queue.put(i)
            print('Put', i)
    async def consumer():
        while True:
            item = await queue.get()
            try:
                print('Doing work on', item)
                await asyncio.sleep(0.01)  # Simulate some work with a sleep
            finally:
                queue.task_done()
    import tornado.ioloop
    tornado.ioloop.IOLoop.current().spawn_callback(consumer)
    await producer()
    await queue.join()
    assert queue._unfinished_tasks == 0

@pytest.mark.asyncio
async def test_join_timeout():
    queue = Queue(maxsize=2)
    with pytest.raises(asyncio.TimeoutError):
        await queue.join(timeout=0.1)
    assert queue._unfinished_tasks == 2  # Ensure tasks are still pending after timeout

@pytest.mark.asyncio
async def test_join_zero_timeout():
    queue = Queue(maxsize=2)
    await queue.put(1)
    await queue.put(2)
    start_time = asyncio.get_event_loop().time()
    await queue.join(timeout=0)
    end_time = asyncio.get_event_loop().time()
    assert end_time - start_time < 0.1  # Ensure join with zero timeout returns immediately

@pytest.mark.asyncio
async def test_join_valid_timeout():
    queue = Queue(maxsize=2)
    async def producer():
        for i in range(2):
            await queue.put(i)
    async def consumer():
        while True:
            item = await queue.get()
            print('Doing work on', item)
            await asyncio.sleep(0.01)  # Simulate some work with a sleep
            queue.task_done()
    import tornado.ioloop
    tornado.ioloop.IOLoop.current().spawn_callback(consumer)
    await producer()
    start_time = asyncio.get_event_loop().time()
    await queue.join(timeout=1)  # Ensure join with valid timeout completes successfully
    end_time = asyncio.get_event_loop().time()
    assert end_time - start_time >= 0.95 and end_time - start_time <= 1.05  # Allow some tolerance for timing
