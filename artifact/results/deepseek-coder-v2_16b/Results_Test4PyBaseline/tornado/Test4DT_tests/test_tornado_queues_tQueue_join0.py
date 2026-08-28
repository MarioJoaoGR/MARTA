# Module: tornado.queues
# test_queues.py
from tornado.queues import Queue
import pytest
import asyncio

@pytest.fixture
def queue():
    return Queue(maxsize=2)

@pytest.mark.asyncio
async def test_put_and_get(queue):
    await queue.put(1)
    assert queue.qsize() == 1
    item = await queue.get()
    assert item == 1
    assert queue.qsize() == 0

@pytest.mark.asyncio
async def test_join_without_tasks():
    queue = Queue(maxsize=2)
    with pytest.raises(asyncio.TimeoutError):
        await queue.join(timeout=0.1)

@pytest.mark.asyncio
async def test_task_done_increments_unfinished_tasks(queue):
    assert queue.qsize() == 0
    assert queue._unfinished_tasks == 0
    item = await queue.get()
    queue.task_done()
    assert queue._unfinished_tasks == 0

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
