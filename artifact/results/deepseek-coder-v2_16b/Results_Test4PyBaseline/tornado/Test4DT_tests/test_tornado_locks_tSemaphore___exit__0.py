
# Module: tornado.locks
import pytest
from tornado.locks import Semaphore
from tornado.ioloop import IOLoop
from tornado.concurrent import Future
import asyncio
from tornado import gen  # Importing gen from tornado for compatibility with the code

# Test creating a Semaphore with an initial value
def test_semaphore_init():
    sem = Semaphore(2)  # Create a semaphore with an initial value of 2
    assert sem._value == 2

# Test acquiring and releasing the semaphore in an asynchronous context
async def test_semaphore_acquire_release():
    sem = Semaphore(2)  # Create a semaphore with an initial value of 2
    
    async def worker(worker_id):
        await sem.acquire()  # Acquire the semaphore
        try:
            assert sem._value == 1  # Check that the semaphore has been acquired
            print("Worker %d is working" % worker_id)
            await asyncio.sleep(0)  # Simulate work with a sleep-like operation
        finally:
            sem.release()  # Release the semaphore
    
    await asyncio.gather(*[worker(i) for i in range(3)])  # Join all workers
    assert sem._value == 2  # Check that the semaphore has been released

# Test using `async with` for context management
async def test_semaphore_context_management():
    sem = Semaphore(2)  # Create a semaphore with an initial value of 2
    
    async def worker(worker_id):
        async with sem:
            assert sem._value == 1  # Check that the semaphore has been acquired within the context
            print("Worker %d is working" % worker_id)
            await asyncio.sleep(0)  # Simulate work with a sleep-like operation
    
    await asyncio.gather(*[worker(i) for i in range(3)])  # Join all workers
    assert sem._value == 2  # Check that the semaphore has been released after the context ends

# Test using `.acquire()` as a context manager for compatibility
@pytest.mark.asyncio
async def test_semaphore_context_manager():
    sem = Semaphore(2)  # Create a semaphore with an initial value of 2
    
    @gen.coroutine
    def worker(worker_id):
        with (yield sem.acquire()):
            assert sem._value == 1  # Check that the semaphore has been acquired within the context
            print("Worker %d is working" % worker_id)
            yield gen.sleep(0)  # Simulate using some resource
    
    IOLoop.current().run_sync(lambda: asyncio.gather([worker(i) for i in range(3)]))  # Run the async tasks
    assert sem._value == 2  # Check that the semaphore has been released after the context ends
