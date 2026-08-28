
import pytest
from tornado.locks import Semaphore
from tornado.concurrent import Future
from collections import deque
import asyncio

# Ensure reliable doctest output: resolve Futures one at a time.
futures_q = deque([Future() for _ in range(3)])

async def simulator(futures):
    for f in futures:
        await asyncio.sleep(0)  # Simulate the asynchronous passage of time
        await asyncio.sleep(0)
        f.set_result(None)

# Mock IOLoop and add the simulator callback
class MockIOLoop:
    def __init__(self):
        self._callbacks = []
    
    def add_callback(self, func, *args):
        self._callbacks.append((func, args))
    
    def run_sync(self, coro):
        asyncio.run(coro())

# Mock IOLoop for testing
@pytest.fixture(scope="module")
def mock_ioloop():
    ioloop = MockIOLoop()
    return ioloop

# Set up the test environment
@pytest.fixture(scope="module")
def semaphore():
    return Semaphore(2)

# Test for acquiring and releasing a semaphore
@pytest.mark.asyncio
async def test_acquire_release(semaphore):
    async def worker(worker_id):
        await semaphore.acquire()
        try:
            print("Worker %d is working" % worker_id)
            # Simulate accessing a shared resource
            futures_q.popleft().set_result(None)
        finally:
            print("Worker %d is done" % worker_id)
            semaphore.release()
    
    async def runner():
        await asyncio.gather(*[worker(i) for i in range(3)])
    
    # Run the async functions using asyncio
    await runner()

# Test for releasing a semaphore with an invalid initial value
def test_invalid_initial_value():
    with pytest.raises(ValueError):
        Semaphore(-1)
