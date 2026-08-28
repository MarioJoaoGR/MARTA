
import pytest
from tornado import locks
import asyncio

@pytest.fixture(scope="function")
def lock():
    return locks.Lock()

# Test valid input using async with statement
@pytest.mark.asyncio
async def test_valid_input_async_with(lock):
    async with lock:
        assert lock._block.locked() is True

# Test releasing an unlocked lock, should raise RuntimeError
def test_error_case_release_unlocked(lock):
    lock._block = locks.BoundedSemaphore(value=0)  # Force the lock to be unlocked
    with pytest.raises(RuntimeError):
        lock.release()

# Test acquiring the lock without using async with or context manager, should raise RuntimeError
@pytest.mark.asyncio
async def test_invalid_input_acquire_without_context(lock):
    with pytest.raises(RuntimeError):
        await lock.acquire()  # Attempt to acquire without context manager
