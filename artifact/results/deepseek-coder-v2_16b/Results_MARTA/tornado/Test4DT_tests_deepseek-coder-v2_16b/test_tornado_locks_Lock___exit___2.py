
import pytest
from tornado import locks
import asyncio
from unittest.mock import patch

# Scenario 1: Test valid usage of async with Lock
@pytest.mark.asyncio
async def test_valid_async_with():
    lock = locks.Lock()
    assert not lock._block.locked(), "Lock should start unlocked"
    
    async with lock:
        assert lock._block.locked(), "Lock should be acquired after async with"
    
    assert not lock._block.locked(), "Lock should be released after async with context manager exits"

# Scenario 2: Test releasing an unlocked lock raises RuntimeError
@pytest.mark.asyncio
async def test_invalid_release():
    lock = locks.Lock()
    with pytest.raises(RuntimeError):
        lock.release()

# Scenario 3: Test acquire method with timeout
@pytest.mark.asyncio
async def test_acquire_timeout():
    lock = locks.Lock()
    lock.acquire()
    
    with patch('tornado.locks.time.sleep', asyncio.coroutine(lambda t: asyncio.sleep(t))):
        with pytest.raises(asyncio.TimeoutError):
            await lock.acquire(timeout=0.01)
