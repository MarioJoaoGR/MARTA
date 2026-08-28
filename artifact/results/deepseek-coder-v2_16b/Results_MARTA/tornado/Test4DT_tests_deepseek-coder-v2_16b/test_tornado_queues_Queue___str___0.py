
import pytest
from tornado.queues import Queue
from tornado.ioloop import IOLoop
import asyncio

# Test for initializing a queue with maxsize=0 (unbounded)
def test_queue_maxsize_zero():
    q = Queue(maxsize=0)
    assert q._maxsize == 0

# Test for adding items to the queue when maxsize is not exceeded
@pytest.mark.asyncio
async def test_put_when_not_full():
    q = Queue(maxsize=2)
    await q.put(1)
    await q.put(2)
    assert len(q._queue) == 2

# Test for adding items to the queue when maxsize is exceeded
@pytest.mark.asyncio
async def test_put_when_full():
    q = Queue(maxsize=2)
    await q.put(1)
    await q.put(2)
    with pytest.raises(Exception):  # Expect a blocking put to raise an exception
        await q.put(3)

# Test for retrieving items from the queue when it is not empty
@pytest.mark.asyncio
async def test_get_when_not_empty():
    q = Queue(maxsize=2)
    await q.put(1)
    item = await q.get()
    assert item == 1

# Test for retrieving items from the queue when it is empty
@pytest.mark.asyncio
async def test_get_when_empty():
    q = Queue(maxsize=2)
    with pytest.raises(Exception):  # Expect a blocking get to raise an exception
        await q.get()

# Test for marking tasks as done after retrieval
@pytest.mark.asyncio
async def test_task_done():
    q = Queue(maxsize=2)
    await q.put(1)
    item = await q.get()
    assert len(q._queue) == 0
    q.task_done()
    assert q._unfinished_tasks == 0

# Test for joining the queue to wait until all tasks are done
@pytest.mark.asyncio
async def test_join():
    q = Queue(maxsize=2)
    await q.put(1)
    IOLoop.current().spawn_callback(lambda: asyncio.ensure_future(q._consume()))
    await asyncio.sleep(0.1)  # Wait for the consumer to start
    assert len(q._queue) == 1
    q.task_done()
    await q.join()
    assert len(q._queue) == 0
