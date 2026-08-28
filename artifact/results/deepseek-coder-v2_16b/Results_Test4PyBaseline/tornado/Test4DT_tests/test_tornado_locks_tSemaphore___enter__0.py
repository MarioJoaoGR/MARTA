# Module: tornado.locks
import pytest
from tornado.locks import Semaphore
from tornado.concurrent import Future
import asyncio

# Test the initialization of a Semaphore instance
def test_semaphore_initialization():
    sem = Semaphore(2)
    assert sem._value == 2

# Test initializing a Semaphore with a negative value, which should raise a ValueError
def test_semaphore_negative_value():
    with pytest.raises(ValueError):
        Semaphore(-1)

# Test acquiring and releasing a permit from the semaphore
async def test_acquire_release():
    sem = Semaphore(2)
    assert sem._value == 2
    
    await sem.acquire()
    assert sem._value == 1
    
    sem.release()
    assert sem._value == 2

# Test acquiring a permit when the semaphore is at zero, which should block until a release occurs
async def test_acquire_block():
    sem = Semaphore(0)
    future = Future()
    
    async def acquire_semaphore():
        await sem.acquire()
        nonlocal future
        future.set_result(None)
    
    # Start the acquisition in a separate task
    asyncio.create_task(acquire_semaphore())
    
    # Wait for the future to be set, indicating that the acquire has started
    await asyncio.wait([future])
    
    sem.release()
    await sem.acquire()
    assert sem._value == 0

# Test using a Semaphore as an async context manager
async def test_context_manager():
    sem = Semaphore(2)
    
    async with sem:
        assert sem._value == 1
        # Simulate work, which might be a Future or similar object
        await asyncio.sleep(0)
    
    assert sem._value == 2

# Test the deprecated `with` statement for Semaphore, which should raise a RuntimeError
def test_deprecated_context_manager():
    sem = Semaphore(2)
    with pytest.raises(RuntimeError):
        with sem:
            pass
