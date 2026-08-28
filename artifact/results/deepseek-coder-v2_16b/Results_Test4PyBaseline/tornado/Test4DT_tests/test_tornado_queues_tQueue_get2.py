
# Module: tornado.queues
from tornado.queues import Queue
import pytest
import asyncio

@pytest.fixture
def queue():
    return Queue(maxsize=2)

@pytest.mark.asyncio
async def test_get_immediate_retrieval(queue):
    # Put an item into the queue
    await queue.put(0)
    
    # Get the item immediately
    item = await queue.get()
    assert item == 0
    assert len(queue._queue) == 0

@pytest.mark.asyncio
async def test_get_with_timeout(queue):
    with pytest.raises(asyncio.TimeoutError):
        await queue.get(timeout=0.1)

@pytest.mark.asyncio
async def test_get_with_timedelta_timeout(queue):
    # Put an item into the queue
    await queue.put(0)
    
    # Get the item with a timedelta timeout
    future = asyncio.Future()
    queue._getters.append(future)  # Simulate the presence of getters waiting for items
    start_time = asyncio.get_event_loop().time()
    with pytest.raises(asyncio.TimeoutError):
        await queue.get(timeout=1)  # Should raise TimeoutError after a timeout
    end_time = asyncio.get_event_loop().time()
    assert (end_time - start_time) >= 1  # Ensure the timeout is respected and exceeds or equals 1 second

@pytest.mark.asyncio
async def test_get_clears_timed_out_getters(queue):
    future = asyncio.Future()
    queue._getters.append(future)  # Simulate a getter waiting for an item
    await asyncio.sleep(0.1)  # Wait for a short period to ensure the timeout is cleared
    assert len(queue._getters) == 0  # Ensure the timed-out future is removed from getters list

@pytest.mark.asyncio
async def test_get_with_timeout_preempted(queue):
    # Put an item into the queue
    await queue.put(0)
    
    # Start a task that waits for the item but preempts before it can get the item
    async def getter():
        with pytest.raises(asyncio.TimeoutError):
            await queue.get(timeout=1)  # Should raise TimeoutError after a timeout
    
    # Run the getter in another task to ensure it runs concurrently
    await asyncio.gather(getter(), queue.put(0))
