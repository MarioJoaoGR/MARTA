
import pytest
from tornado.queues import Queue
from tornado.ioloop import IOLoop
from unittest.mock import patch, MagicMock
import asyncio

@pytest.mark.asyncio
async def test_valid_case():
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

    with patch('tornado.ioloop.IOLoop.current') as mock_ioloop, \
         patch('tornado.ioloop.IOLoop.run_sync'):
        mock_ioloop.return_value.run_sync.side_effect = lambda f: IOLoop.current().run_sync(f)
        mock_ioloop.return_value.spawn_callback.side_effect = lambda f: IOLoop.current().spawn_callback(f)

        with patch('tornado.queues.Queue.put', new=MagicMock()) as mock_put, \
             patch('tornado.queues.Queue.get', new=MagicMock()) as mock_get:
            mock_put.side_effect = lambda item: None
            mock_get.side_effect = lambda: None

            IOLoop.current().run_sync(lambda: producer())

    # Wait for the consumer to finish all tasks
    await q.join()
    print('Done')

if __name__ == "__main__":
    pytest.main([__file__])
