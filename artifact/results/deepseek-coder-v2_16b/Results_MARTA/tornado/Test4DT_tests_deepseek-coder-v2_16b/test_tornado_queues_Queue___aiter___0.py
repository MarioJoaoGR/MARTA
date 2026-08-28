
import pytest
from tornado.queues import Queue
from tornado.ioloop import IOLoop
from tornado import gen

@pytest.fixture
def queue():
    return Queue(maxsize=2)

@pytest.mark.asyncio
async def test_queue_put_and_get(queue):
    await queue.put(0)
    item = await queue.get()
    assert item == 0

@pytest.mark.asyncio
async def test_queue_join_wait(queue):
    async def consumer():
        async for _ in queue:
            pass

    IOLoop.current().spawn_callback(consumer)
    await queue.put(1)
    await queue.put(2)
    assert not queue._finished.is_set()
    await queue.join()
    assert queue._finished.is_set()

@pytest.mark.asyncio
async def test_queue_task_done(queue):
    async def producer():
        for item in range(3):
            await queue.put(item)

    async def consumer():
        async for _ in queue:
            await gen.sleep(0.01)
            queue.task_done()

    IOLoop.current().spawn_callback(consumer)
    await producer()
    assert not queue._finished.is_set()
    await queue.join()
    assert queue._finished.is_set()

@pytest.mark.asyncio
async def test_queue_maxsize_limit(queue):
    async def producer():
        for item in range(3):
            await queue.put(item)
            print('Put %s' % item)

    async def consumer():
        async for _ in queue:
            await gen.sleep(0.01)
            queue.task_done()

    IOLoop.current().spawn_callback(consumer)
    await producer()
    assert not queue._finished.is_set()
    with pytest.raises(Exception):  # Expect a condition where the queue is full and put will wait
        await queue.put(3)
