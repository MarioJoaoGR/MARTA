
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
        await asyncio.sleep(0)  # Simulate the asynchronous passage of time
        await asyncio.sleep(0)
        f.set_result(None)

IOLoop.current().add_callback(simulator, list(futures_q))

def use_some_resource():
    return futures_q.popleft()  # Simulate accessing a shared resource

@pytest.fixture
def semaphore():
    return Semaphore(2)

@pytest.mark.asyncio
async def test_semaphore_with_context_manager(semaphore):
    async with semaphore:
        print("Worker is working")
        await use_some_resource()
    # Now the semaphore has been released.
    print("Worker is done")

@pytest.mark.asyncio
async def test_semaphore_without_context_manager(semaphore):
    async with semaphore:
        print("Worker is working")
        await use_some_resource()
    # Now the semaphore has been released.
    print("Worker is done")

@pytest.mark.asyncio
async def test_semaphore_release(semaphore):
    assert semaphore._value == 2
    semaphore.release()
    assert semaphore._value == 3
