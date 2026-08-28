
# Module: tornado.queues
# test_queues.py
from tornado.queues import Queue
import pytest
import asyncio

@pytest.fixture
def create_queue():
    return Queue(maxsize=2)

@pytest.mark.asyncio
async def test_put_and_get(create_queue):
    q = create_queue
    await q.put(1)
    assert q.qsize() == 1
    item = await q.get()
    assert item == 1
    assert q.qsize() == 0

@pytest.mark.asyncio
async def test_full_queue(create_queue):
    q = create_queue
    for i in range(2):
        await q.put(i)
    with pytest.raises(Exception):
        await q.put(3)  # Should raise an exception because the queue is full

@pytest.mark.asyncio
async def test_empty_queue(create_queue):
    q = create_queue
    with pytest.raises(Exception):
        await q.get()  # Should raise an exception because the queue is empty

@pytest.mark.asyncio
async def test_task_done(create_queue):
    q = create_queue
    await q.put(1)
    item = await q.get()
    q.task_done()
    assert q.qsize() == 0
    with pytest.raises(Exception):
        q.task_done()  # Should raise an exception because the task is already done

@pytest.mark.asyncio
async def test_join(create_queue):
    q = create_queue
    async def producer():
        for i in range(5):
            await q.put(i)
            print('Put %s' % i)

    async def consumer():
        while True:
            item = await q.get()
            try:
                print('Doing work on %s' % item)
                await asyncio.sleep(0.01)
            finally:
                q.task_done()

    loop = asyncio.get_event_loop()
    loop.create_task(consumer())
    producer_future = asyncio.ensure_future(producer(), loop=loop)
    await q.join()
    assert q.qsize() == 0
    print('Done')
