
import pytest
from tornado.queues import Queue
from tornado.ioloop import IOLoop
from unittest.mock import patch, MagicMock
import asyncio

@pytest.mark.asyncio
async def test_valid_inputs():
    q = Queue(maxsize=2)

    async def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)

    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await asyncio.sleep(0.01)
            finally:
                q.task_done()

    async def main():
        IOLoop.current().spawn_callback(consumer)
        await producer()
        await q.join()
        print('Done')

    with patch('tornado.ioloop.IOLoop'):
        with patch('tornado.gen', MagicMock()):
            IOLoop.current().run_sync(main)
