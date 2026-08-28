
import pytest
from tornado.queues import Queue
from tornado.ioloop import IOLoop
import asyncio

@pytest.mark.asyncio
async def test_queue_maxsize_0():
    q = Queue(maxsize=0)
    
    # Test putting items into the queue with maxsize 0 (unbounded)
    await q.put(1)
    assert len(q._queue) == 1, "Queue size should be 1 after one put"
    
    await q.put(2)
    assert len(q._queue) == 2, "Queue size should be 2 after two puts"
    
    # Test getting items from the queue with maxsize 0 (unbounded)
    item = await q.get()
    assert item == 1, "First item in the queue should be 1"
    assert len(q._queue) == 1, "Queue size should be 1 after one get"
    
    item = await q.get()
    assert item == 2, "Second item in the queue should be 2"
    assert len(q._queue) == 0, "Queue size should be 0 after two gets"
    
    # Test task_done and join with maxsize 0 (unbounded)
    q.task_done()
    await q.join()
    assert q._unfinished_tasks == 0, "All tasks should be done"

@pytest.mark.asyncio
async def test_queue_maxsize_positive():
    q = Queue(maxsize=2)
    
    # Test putting items into the queue with maxsize 2 (bounded)
    await q.put(1)
    assert len(q._queue) == 1, "Queue size should be 1 after one put"
    
    await q.put(2)
    assert len(q._queue) == 2, "Queue size should be 2 after two puts"
    
    with pytest.raises(asyncio.QueueFull):
        await q.put(3)  # This should raise QueueFull because maxsize is 2
    
    # Test getting items from the queue with maxsize 2 (bounded)
    item = await q.get()
    assert item == 1, "First item in the queue should be 1"
    assert len(q._queue) == 1, "Queue size should be 1 after one get"
    
    item = await q.get()
    assert item == 2, "Second item in the queue should be 2"
    assert len(q._queue) == 0, "Queue size should be 0 after two gets"
    
    # Test task_done and join with maxsize 2 (bounded)
    q.task_done()
    await q.join()
    assert q._unfinished_tasks == 0, "All tasks should be done"
