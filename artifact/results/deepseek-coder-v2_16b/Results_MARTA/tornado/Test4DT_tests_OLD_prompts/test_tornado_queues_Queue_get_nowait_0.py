
import pytest
from tornado.queues import Queue, QueueEmpty
from tornado.ioloop import IOLoop
from tornado import gen

# Test for the Queue class initialization with maxsize parameter
def test_queue_initialization():
    q = Queue(maxsize=2)
    assert q._maxsize == 2

# Test for adding items to the queue by producer coroutine
@pytest.mark.asyncio
async def test_producer_consumer():
    q = Queue(maxsize=2)

    async def consumer():
        while True:
            item = await q.get()
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()

    async def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)

    # Start consumer without waiting (since it never finishes).
    IOLoop.current().spawn_callback(consumer)
    await producer()  # Wait for producer to put all tasks.
    await q.join()     # Wait for consumer to finish all tasks.
    print('Done')      # Print that all tasks are done

# Test for the Queue class with maxsize set to 0 (unbounded)
def test_queue_unbounded():
    q = Queue(maxsize=0)
    assert q._maxsize == 0

# Test for getting an item from an empty queue without blocking
def test_get_nowait_from_empty_queue():
    q = Queue(maxsize=2)
    with pytest.raises(QueueEmpty):
        q.get_nowait()
