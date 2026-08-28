
import pytest
from tornado.queues import Queue
import asyncio

@pytest.mark.asyncio
async def test_queue_creation():
    q = Queue(maxsize=2)
    assert isinstance(q, Queue), "Queue instance should be of type Queue"

@pytest.mark.asyncio
async def test_put_and_get():
    q = Queue(maxsize=2)
    await q.put(1)
    item = await q.get()
    assert item == 1, "The put and get operations should return the same item"

@pytest.mark.asyncio
async def test_full_queue():
    q = Queue(maxsize=2)
    await q.put(1)
    await q.put(2)
    with pytest.raises(Exception):  # We need to mock the behavior of put when full
        await q.put(3)

@pytest.mark.asyncio
async def test_task_done():
    q = Queue(maxsize=2)
    await q.put(1)
    item = await q.get()
    assert q._unfinished_tasks == 0, "The task should be marked as done after get"

@pytest.mark.asyncio
async def test_join():
    q = Queue(maxsize=2)
    async def producer():
        for item in range(3):
            await q.put(item)
    async def consumer():
        while True:
            item = await q.get()
            print('Doing work on %s' % item)
            await asyncio.sleep(0.01)  # Mock sleep for demonstration purposes
            q.task_done()
    
    producer_task = asyncio.create_task(producer())
    consumer_task = asyncio.create_task(consumer())
    
    await asyncio.gather(producer_task, consumer_task)
    assert q._unfinished_tasks == 0, "All tasks should be done after join"
