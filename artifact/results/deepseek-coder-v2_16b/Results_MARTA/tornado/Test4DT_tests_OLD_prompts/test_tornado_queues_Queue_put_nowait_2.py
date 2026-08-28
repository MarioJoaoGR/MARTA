
import pytest
from tornado.queues import Queue, QueueFull, QueueEmpty
from unittest.mock import patch

# Test valid input scenario
@pytest.mark.asyncio
async def test_valid_input():
    from tornado.queues import Queue
    q = Queue(maxsize=2)
    
    async def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)
    
    with patch('tornado.queues.Queue._consume_expired', return_value=None):
        await producer()  # Wait for producer to put all tasks.
        assert not q.full(), "Queue should not be full after putting items"
        
        await q.join()       # Wait for consumer to finish all tasks.
        print('Done')

# Test edge case scenario with None and empty list
@pytest.mark.asyncio
async def test_edge_case():
    from tornado.queues import Queue
    q = Queue()
    
    async def producer():
        for item in []:
            await q.put(item)
    
    with pytest.raises(ValueError):
        q.__init__(maxsize=None)
        
    with patch('tornado.queues.Queue._consume_expired', return_value=None):
        await producer()  # Wait for producer to put all tasks.
        assert not q.full(), "Queue should not be full after putting items"
        
        await q.join()       # Wait for consumer to finish all tasks.
        print('Done')

# Test invalid input scenario raising exceptions with invalid inputs
@pytest.mark.asyncio
async def test_invalid_input():
    from tornado.queues import Queue, QueueFull, QueueEmpty
    q = Queue(maxsize=1)
    
    async def producer():
        for item in range(2):
            await q.put(item)
            print('Put %s' % item)
    
    with pytest.raises(QueueFull):
        await q.put_nowait(2)
        
    with pytest.raises(QueueEmpty):
        q.get_nowait()
        
    with patch('tornado.queues.Queue._consume_expired', return_value=None):
        await producer()  # Wait for producer to put all tasks.
        assert not q.full(), "Queue should not be full after putting items"
        
        await q.join()       # Wait for consumer to finish all tasks.
        print('Done')
