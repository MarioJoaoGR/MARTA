
import pytest
from tornado.queues import Queue
from unittest.mock import patch, MagicMock
import asyncio

@pytest.fixture(scope="function")
def setup_queue():
    q = Queue(maxsize=2)
    return q

@pytest.mark.asyncio
@pytest.mark.parametrize("item", [0, 1, 2, 3, 4])
async def test_valid_inputs(setup_queue, item):
    from tornado import gen
    async def producer():
        await setup_queue.put(item)
        print('Put %s' % item)
    
    async def consumer():
        async for item in setup_queue:
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                setup_queue.task_done()
    
    with patch('tornado.ioloop.IOLoop.current') as mock_ioloop, \
         patch('tornado.queues.Queue._put', new_callable=MagicMock), \
         patch('tornado.queues.Queue._get', new_callable=MagicMock):
        mock_ioloop.return_value = MagicMock()
        mock_ioloop.return_value.run_sync.side_effect = lambda coro: asyncio.run(coro())
        
        await setup_queue.put(item)  # Put an item into the queue
        assert len(setup_queue._queue) == 1, "Queue should have one item"
        
        consumer_task = asyncio.create_task(consumer())
        producer_task = asyncio.create_task(producer())
        
        await asyncio.gather(consumer_task, producer_task)
        
        assert len(setup_queue._queue) == 0, "Queue should be empty after all items are processed"

@pytest.mark.asyncio
@pytest.mark.parametrize("item", [None, [], None])
async def test_edge_cases(setup_queue, item):
    from tornado import gen
    async def producer():
        if item is not None:
            await setup_queue.put(item)
            print('Put %s' % item)
    
    async def consumer():
        while True:
            item = await setup_queue.get()
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                setup_queue.task_done()
    
    with patch('tornado.ioloop.IOLoop.current') as mock_ioloop, \
         patch('tornado.queues.Queue._put', new_callable=MagicMock), \
         patch('tornado.queues.Queue._get', new_callable=MagicMock):
        mock_ioloop.return_value = MagicMock()
        mock_ioloop.return_value.run_sync.side_effect = lambda coro: asyncio.run(coro())
        
        producer_task = asyncio.create_task(producer())
        consumer_task = asyncio.create_task(consumer())
        
        await asyncio.gather(producer_task, consumer_task)
        
        assert setup_queue._unfinished_tasks == 0, "All tasks should be done"

@pytest.mark.asyncio
@pytest.mark.parametrize("item", ["string", object()])
async def test_invalid_inputs(setup_queue, item):
    from tornado import gen
    async def producer():
        with pytest.raises(TypeError):
            await setup_queue.put(item)
    
    with patch('tornado.ioloop.IOLoop.current') as mock_ioloop, \
         patch('tornado.queues.Queue._put', new_callable=MagicMock), \
         patch('tornado.queues.Queue._get', new_callable=MagicMock):
        mock_ioloop.return_value = MagicMock()
        mock_ioloop.return_value.run_sync.side_effect = lambda coro: asyncio.run(coro())
        
        await producer()
