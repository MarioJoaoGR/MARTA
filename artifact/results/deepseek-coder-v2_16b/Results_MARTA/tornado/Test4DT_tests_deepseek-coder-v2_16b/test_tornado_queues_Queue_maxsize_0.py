
import pytest
from tornado.queues import Queue
from tornado.ioloop import IOLoop
import asyncio

@pytest.mark.asyncio
async def test_queue_creation():
    q = Queue(maxsize=2)
    assert q.maxsize == 2, f"Expected maxsize to be 2 but got {q.maxsize}"

@pytest.mark.asyncio
async def test_put_and_get():
    q = Queue(maxsize=2)
    await q.put(1)
    item = await q.get()
    assert item == 1, f"Expected to get 1 but got {item}"

@pytest.mark.asyncio
async def test_task_done_and_join():
    q = Queue(maxsize=2)
    await q.put(1)
    q.task_done()
    assert q._unfinished_tasks == 0, f"Expected unfinished tasks to be 0 but got {q._unfinished_tasks}"
    await q.join()
    assert q._unfinished_tasks == 0, f"Expected unfinished tasks to be 0 after join but got {q._unfinished_tasks}"

@pytest.mark.asyncio
async def test_queue_full():
    q = Queue(maxsize=2)
    await q.put(1)
    await q.put(2)
    with pytest.raises(QueueFull):
        await q.put(3)  # This should raise QueueFull error because the queue is full
