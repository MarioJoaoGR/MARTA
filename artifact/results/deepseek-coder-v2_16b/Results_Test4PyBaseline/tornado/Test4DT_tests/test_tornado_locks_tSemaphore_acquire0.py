# Module: tornado.locks
# test_semaphore.py
import pytest
from tornado.locks import Semaphore
from tornado.ioloop import IOLoop
import asyncio

@pytest.fixture
def semaphore():
    return Semaphore(2)

@pytest.mark.asyncio
async def test_acquire_release(semaphore):
    # Test acquiring and releasing the semaphore twice, allowing two workers to run concurrently
    await semaphore.acquire()
    assert semaphore._value == 1
    task1 = asyncio.create_task(semaphore.acquire())
    await asyncio.sleep(0)  # Allow other tasks to run
    await semaphore.release()
    await task1
    assert semaphore._value == 1
    await semaphore.release()
    assert semaphore._value == 2

@pytest.mark.asyncio
async def test_context_manager(semaphore):
    # Test using the semaphore as a context manager
    async with semaphore:
        assert semaphore._value == 1
        await asyncio.sleep(0)
    assert semaphore._value == 2

@pytest.mark.asyncio
async def test_timeout_acquire(semaphore):
    # Test acquiring the semaphore with a timeout, expecting it to time out
    with pytest.raises(asyncio.TimeoutError):
        await asyncio.wait_for(semaphore.acquire(), timeout=0.1)

@pytest.mark.asyncio
async def test_release_below_zero():
    # Test releasing the semaphore below zero, which should raise a ValueError
    with pytest.raises(ValueError):
        Semaphore(-1)

if __name__ == "__main__":
    pytest.main()
