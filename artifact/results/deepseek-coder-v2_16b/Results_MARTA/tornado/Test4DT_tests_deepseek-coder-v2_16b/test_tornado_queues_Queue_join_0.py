
import pytest
from tornado.queues import Queue
import asyncio
from tornado.ioloop import IOLoop

@pytest.mark.asyncio
async def test_valid_case():
    q = Queue(maxsize=2)
    
    assert q._maxsize == 2
    assert len(q._getters) == 0
    assert len(q._putters) == 0

    async def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)

    async def main():
        IOLoop.current().spawn_callback(producer())
        await asyncio.sleep(0.1)  # Wait a bit for the producer to put all tasks
        assert len(q._putters) == 5
        assert q._unfinished_tasks == 5

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
