
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

# Example runner function to demonstrate usage
async def runner():
    await asyncio.gather(*[worker(i) for i in range(3)])  # Run three worker coroutines concurrently

# Define the test functions
@pytest.mark.asyncio
async def test_semaphore_initialization():
    sem = Semaphore(2)  # Create a semaphore with an initial value of 2
    assert sem._value == 2, "Semaphore initialization failed"

@pytest.mark.asyncio
async def test_acquire_release():
    sem = Semaphore(1)  # Create a semaphore with an initial value of 1
    await sem.acquire()  # Acquire the semaphore before working
    assert sem._value == 0, "Semaphore acquire failed"
    sem.release()  # Release the semaphore after finishing
    assert sem._value == 1, "Semaphore release failed"

@pytest.mark.asyncio
async def test_context_manager():
    sem = Semaphore(1)  # Create a semaphore with an initial value of 1
    async with sem:
        assert sem._value == 0, "Context manager acquire failed"
    assert sem._value == 1, "Context manager release failed"

@pytest.mark.asyncio
async def test_edge_case_none():
    sem = Semaphore(0)  # Create a semaphore with an initial value of 0
    with pytest.raises(ValueError):
        await sem.acquire()  # Attempt to acquire when the semaphore is not available should raise ValueError
