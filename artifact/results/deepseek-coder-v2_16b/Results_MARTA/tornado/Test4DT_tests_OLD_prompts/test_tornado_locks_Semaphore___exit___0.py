
import pytest
from tornado.locks import Semaphore
from tornado.ioloop import IOLoop
from tornado.concurrent import Future
from collections import deque
import asyncio

# Ensure reliable doctest output: resolve Futures one at a time.
futures_q = deque([Future() for _ in range(3)])

async def simulator(futures):
    for f in futures:
        # simulate the asynchronous passage of time
        await asyncio.sleep(0)
        await asyncio.sleep(0)
        f.set_result(None)

IOLoop.current().add_callback(simulator, list(futures_q))

def use_some_resource():
    return futures_q.popleft()

# Test for Semaphore initialization with a valid value
def test_semaphore_init_valid_value():
    sem = Semaphore(2)
    assert sem._value == 2

# Test for Semaphore initialization with an invalid value (should raise ValueError)
def test_semaphore_init_invalid_value():
    with pytest.raises(ValueError):
        Semaphore(-1)

# Test for acquiring and releasing the semaphore
@pytest.mark.asyncio
async def test_acquire_release():
    sem = Semaphore(2)
    
    async def worker(worker_id):
        await sem.acquire()
        try:
            print("Worker %d is working" % worker_id)
            await use_some_resource()
        finally:
            print("Worker %d is done" % worker_id)
            sem.release()
    
    async def runner():
        await asyncio.gather(*[worker(i) for i in range(3)])
    
    await runner()

# Test for using the semaphore as a context manager with async with
@pytest.mark.asyncio
async def test_semaphore_context_manager():
    sem = Semaphore(2)
    
    async def worker(worker_id):
        async with sem:
            print("Worker %d is working" % worker_id)
            await use_some_resource()
    
    async def runner():
        await asyncio.gather(*[worker(i) for i in range(3)])
    
    await runner()

# Test for using the semaphore as a context manager with old-style context manager (for older Python versions)
@pytest.mark.asyncio
async def test_semaphore_context_manager_old_style():
    sem = Semaphore(2)
    
    @pytest.mark.gen_test
    def worker(worker_id):
        with (yield sem.acquire()):
            print("Worker %d is working" % worker_id)
            yield use_some_resource()
    
    async def runner():
        await asyncio.gather(*[worker(i) for i in range(3)])
    
    await runner()
