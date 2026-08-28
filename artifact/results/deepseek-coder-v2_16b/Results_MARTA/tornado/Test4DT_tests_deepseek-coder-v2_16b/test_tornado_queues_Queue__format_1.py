
import pytest
from tornado.queues import Queue
from tornado.ioloop import IOLoop
import asyncio

@pytest.mark.asyncio
async def test_valid_input():
    q = Queue(maxsize=2)
    assert q.maxsize == 2

    # Put items into the queue
    q.put(1)
    q.put(2)

    # Get items from the queue
    item1 = await asyncio.wait_for(q.get(), timeout=1)
    item2 = await asyncio.wait_for(q.get(), timeout=1)

    assert item1 == 1
    assert item2 == 2
