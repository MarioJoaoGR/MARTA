
import pytest
from tornado import locks
import asyncio

@pytest.fixture
def lock():
    return locks.Lock()

@pytest.mark.asyncio
async def test_valid_async_with(lock):
    assert not lock._block.locked(), "Lock should start unlocked"
    async with lock:
        assert lock._block.locked(), "Lock should be locked after async with"
    assert not lock._block.locked(), "Lock should be released after async with context manager exits"

@pytest.mark.asyncio
async def test_error_release_on_unlocked(lock):
    with pytest.raises(RuntimeError):
        lock.release()

@pytest.mark.asyncio
async def test_invalid_usage_without_async_with(lock):
    with pytest.raises(RuntimeError):
        with lock:
            pass
